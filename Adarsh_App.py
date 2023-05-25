'''
@author: Snehan Kekre -- modified by Adarsh Kuthuru
'''

import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

from sodapy import Socrata

DATE_TIME = "date/time"

st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a Streamlit dashboard that can be used "
            "to analyze motor vehicle collisions in NYC 🗽")


@st.cache_data(persist=True)
def load_data(nrows) -> pd.DataFrame:
    '''
    This function imports data through SODA API and does some cleaning
    '''
    client = Socrata("data.cityofnewyork.us", None)
    client.timeout = 1000
    results = client.get("h9gi-nx95", limit=nrows)
    data = pd.DataFrame.from_records(results)
    return data

def scrub_data(data):
    '''
    This function cleans the dataset before analyzing it
    '''
    # Parse Date and Time
    data['crash_date'] = pd.to_datetime(data['crash_date']).dt.strftime('%Y-%m-%d') 
    data['crash_time'] = pd.to_datetime(data['crash_time'], format='%H:%M').dt.time
    data['crash_date_crash_time'] = pd.to_datetime(data['crash_date'].astype(str) + ' ' + data['crash_time'].astype(str), format = '%Y-%m-%d %H:%M:%S')

    # Drop superfluous data and Rename Columns
    data.dropna(subset=['latitude', 'longitude'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data.columns = data.columns.str.replace(' ', '_')
    data.rename(columns={"crash_date_crash_time": "date/time"}, inplace=True)

    # Convert strings to numerical data
    numeric_data = ['number_of_persons_injured', 'number_of_pedestrians_injured', 'number_of_cyclist_injured', 'number_of_motorist_injured']
    data[numeric_data] = data[numeric_data].apply(pd.to_numeric, errors='coerce')
    data['latitude'] = data['latitude'].astype(float)
    data['longitude'] = data['longitude'].astype(float)
    return data


data = load_data(100000)
clean_data = scrub_data(data)
st.write(clean_data)


st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number of persons injured in vehicle collisions", 0, 19)
st.map(data.query("number_of_persons_injured >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))

st.header("How many collisions occur during a given time of day?")
hour = st.slider("Hour to look at", 0, 23)
data = data[data[DATE_TIME].dt.hour == hour]
st.markdown("Vehicle collisions between %i:00 and %i:00" % (hour, (hour + 1) % 24))

midpoint = (np.average(data["latitude"]), np.average(data["longitude"]))
st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
        "HexagonLayer",
        data=data[['date/time', 'latitude', 'longitude']],
        get_position=["longitude", "latitude"],
        auto_highlight=True,
        radius=100,
        extruded=True,
        pickable=True,
        elevation_scale=4,
        elevation_range=[0, 1000],
        ),
    ],
))


if st.checkbox("Show raw data", False):
    st.subheader("Raw data by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
    st.write(data)

st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
filtered = data[
    (data[DATE_TIME].dt.hour >= hour) & (data[DATE_TIME].dt.hour < (hour + 1))
]
hist = np.histogram(filtered[DATE_TIME].dt.minute, bins=60, range=(0, 60))[0]
chart_data = pd.DataFrame({"minute": range(60), "crashes": hist})

fig = px.bar(chart_data, x='minute', y='crashes', hover_data=['minute', 'crashes'], height=400)
st.write(fig)

st.header("Top 5 dangerous streets by affected class")
select = st.selectbox('Affected class', ['Pedestrians', 'Cyclists', 'Motorists'])

if select == 'Pedestrians':
    st.write(data.query("number_of_pedestrians_injured >= 1")[["on_street_name", "number_of_pedestrians_injured"]].sort_values(by=['number_of_pedestrians_injured'], ascending=False).dropna(how="any")[:5])

elif select == 'Cyclists':
    st.write(data.query("number_of_cyclist_injured >= 1")[["on_street_name", "number_of_cyclist_injured"]].sort_values(by=['number_of_cyclist_injured'], ascending=False).dropna(how="any")[:5])

else:
    st.write(data.query("number_of_motorist_injured >= 1")[["on_street_name", "number_of_motorist_injured"]].sort_values(by=['number_of_motorist_injured'], ascending=False).dropna(how="any")[:5])