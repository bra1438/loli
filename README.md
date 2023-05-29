# Motor-Vehicle-Collision-Analysis-with-Streamlit-App

## Summary of the code:
The objective of this Python code repo is to create a Streamlit application that visualizes and performs exploratory data analysis (EDA) on motor vehicle collisions in New York City (NYC). 

**Dashboard**: [This is the link to Streamlit app hosted on Streamlit cloud server](https://adarshkuthuru-motor-vehicle-collision-anal-srcadarsh-app-l1fegq.streamlit.app/)

The code imports various dependencies such as Streamlit, pandas, numpy, pydeck, plotly.express, and sodapy. 

The main function `gen_dashboard` is responsible for creating the entire application. It first loads the data from the NYC Open Data API using the `load_data` function, which retrieves a specified number of records and performs some initial cleaning.

The `scrub_data` function further cleans the dataset by parsing date and time columns, dropping unnecessary columns, renaming and converting data types, and filtering the data to include only incidents within the NYC metro area.

The application includes several interactive components for data visualization and analysis. It provides two maps (`map_of_the_incident` and `map_of_the_incident_freq_hist`) to visualize the incidents on a map based on different criteria such as the number of injured or killed individuals. Users can select options and adjust sliders to filter and explore the data.

### The first map is a 2-Dimensional (2D) plot of the incident

![1](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-1.jpg)

### The second map is a 3-Dimensional (3D) plot of crash frequency/count of the incident
![2](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-3.jpg)

The code utilizes helper functions defined in the `helper_functions.py` module for additional analysis and visualization. The `exploratory_data_analysis` function in this module provides a range of options for interactive exploratory data analysis on a motor incident dataset in New York City (NYC) as shown below. 
![10](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-2.jpg)

Users can select various visualizations to gain insights into the data. The available options include:

1. **Info:** Displays general information about the dataset, such as column names, data types, and non-null counts.
2. **Missing Value Info:** Identifies and presents columns with missing values, along with their respective counts.
3. **Descriptive Analysis:** Computes and displays descriptive statistics (count, mean, standard deviation, etc.) for numerical variables in the dataset.
4. **Target Analysis:** Allows users to select a target variable and shows a histogram of its values.
5. **Distribution of Numerical Variables:** Plots histograms for selected numerical variables, enabling users to explore their distributions.
6. **Count Plots of Categorical Variables:** Generates count plots (bar charts) for selected categorical variables, providing insights into their distributions.
7. **Box Plots:** Presents box plots for selected numerical variables, helping identify potential outliers and understand the distribution characteristics.
8. **Outlier Analysis:** Performs outlier analysis on numerical variables and presents a table with the number of outliers for each variable.

### Below are some images of the above visualizations as seen in the app.

### Info
![3](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-2.1.jpg)

### Missing Value Info
![4](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-2.2.jpg)

### Descriptive Analysis
![5](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-2.3.jpg)

### Target Analysis
![6](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-2.4.jpg)

### Distribution of Numerical Variables
![7](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-2.5.jpg)

### Box Plots
![8](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-2.6.jpg)

### Outlier Analysis
![9](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-2.7.jpg)

These options empower users to investigate the dataset from various angles, uncover patterns, and identify key insights. The combination of descriptive statistics, visualizations, and outlier analysis supports comprehensive exploratory data analysis and facilitates a better understanding of the motor incident dataset in NYC.

Additionally, the application generates histograms (`gen_chart_hist_by_min`) to show the frequency of incidents during a specific hour and minute of the day. It also creates tables (`create_table_incident_by_street`) to display the top 5 dangerous streets based on the number of injuries or fatalities for pedestrians, cyclists, or motorists.

### Minute-by-minute plot of the frequency of incidents during a specific hour 
![11](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-4.jpg)

### Top streets based on the number of injuries or fatalities for pedestrians, cyclists, or motorists
![12](https://github.com/adarshkuthuru/Motor-Vehicle-Collision-Analysis-with-Streamlit-App/blob/main/images/Analysis-5.jpg)

Overall, this application provides an interactive dashboard for exploring and analyzing motor vehicle collisions in NYC, helping users gain insights into the incidents and their spatial and temporal patterns.

**References:**
1. [Anar Abiyev's GitHub Repo](https://github.com/anarabiyev/EDA_Streamlit_App)
2. [Snehan Kekre's GitHub Repo](https://github.com/snehankekre/Streamlit-Vehicle-Collisions-NYC)
