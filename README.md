# Streamlit-App-Demo

## Summary of the code:
This Python code repo is to create a Streamlit application that visualizes and performs exploratory data analysis (EDA) on motor vehicle collisions in New York City (NYC). 

**Dashboard**: [This is the link to the Streamlit app hosted on Streamlit cloud server](https://adarshkuthuru-streamlit-app-demo-adarsh-app-e3clwl.streamlit.app/)

The code imports various dependencies such as Streamlit, pandas, numpy, pydeck, plotly.express, and sodapy. 

The main function `gen_dashboard` is responsible for creating the entire application. It first loads the data from the NYC Open Data API using the `load_data` function, which retrieves a specified number of records and performs some initial cleaning.

The `scrub_data` function further cleans the dataset by parsing date and time columns, dropping unnecessary columns, renaming and converting data types, and filtering the data to include only incidents within the NYC metro area.

The application includes several interactive components for data visualization and analysis. It provides two maps (`map_of_the_incident` and `map_of_the_incident_freq_hist`) to visualize the incidents on a map based on different criteria such as the number of injured or killed individuals. Users can select options and adjust sliders to filter and explore the data.

Additionally, the application generates histograms (`gen_chart_hist_by_min`) to show the frequency of incidents during a specific hour and minute of the day. It also creates tables (`create_table_incident_by_street`) to display the top 5 dangerous streets based on the number of injuries or fatalities for pedestrians, cyclists, or motorists.

The code utilizes helper functions defined in the `helper_functions.py` module for additional analysis and visualization. The `exploratory_data_analysis` function in this module provides a range of options for interactive exploratory data analysis on a motor incident dataset in New York City (NYC). 

Users can select various visualizations to gain insights into the data. The available options include:

1. **Info:** Displays general information about the dataset, such as column names, data types, and non-null counts.
2. **Missing Value Info:** Identifies and presents columns with missing values, along with their respective counts.
3. **Descriptive Analysis:** Computes and displays descriptive statistics (count, mean, standard deviation, etc.) for numerical variables in the dataset.
4. **Target Analysis:** Allows users to select a target variable and shows a histogram of its values.
5. **Distribution of Numerical Variables:** Plots histograms for selected numerical variables, enabling users to explore their distributions.
6. **Count Plots of Categorical Variables:** Generates count plots (bar charts) for selected categorical variables, providing insights into their distributions.
7. **Box Plots:** Presents box plots for selected numerical variables, helping identify potential outliers and understand the distribution characteristics.
8. **Outlier Analysis:** Performs outlier analysis on numerical variables and presents a table with the number of outliers for each variable.

These options empower users to investigate the dataset from various angles, uncover patterns, and identify key insights. The combination of descriptive statistics, visualizations, and outlier analysis supports comprehensive exploratory data analysis and facilitates a better understanding of the motor incident dataset in NYC.

Overall, this application provides an interactive dashboard for exploring and analyzing motor vehicle collisions in NYC, helping users gain insights into the incidents and their spatial and temporal patterns.

This can be used to perform various cross-sectional analyses of "Motor Vehicle Crashes" data in NYC.

# Anaysis-1: 2-Dimensional (2D) plot of crashes by location

![1](https://github.com/adarshkuthuru/Streamlit-App-Demo/assets/20659563/ec789cad-7321-44d2-982c-04b9cf7833da)

# Anaysis-2: 3-Dimensional (3D) plot of crash frequency/count by location

![2](https://github.com/adarshkuthuru/Streamlit-App-Demo/assets/20659563/b7215624-adf1-47f3-81a0-437e83168a88)

# Anaysis-3: Minute-by-minute analysis

![3](https://github.com/adarshkuthuru/Streamlit-App-Demo/assets/20659563/5738e35d-200f-4a52-8e5e-ef62554487fe)


# Anaysis-4: Top streets by injured person category

![4](https://github.com/adarshkuthuru/Streamlit-App-Demo/assets/20659563/619fbd5f-02a8-448b-9112-5b1c7b7fcd89)
