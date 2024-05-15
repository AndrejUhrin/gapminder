In this project we took 3 datasets from Gapminder website that contain information regarding population, life expectancy and GNI per capita.
After loading the data we had to preprocess them in the following steps:
1. fill the missing values within each datasets
2. transform each dataset into tiny data format, which means that after transformation each dataset had 3 columns consisting of country, year and KPI
3. merge three datasets into one dataframe
After preporcessing we have created two interactive widgets:
1. a year slider to control the year (only one year will be displayed)
2. a multiselect widget for selecting one or more countries
for the dashboard we created a bubble chart that consited of following KPIs:
X axis: Logarithmic Gross Natition Income (GNI) per captia, where we also created that the x value stays as a constant
Y axis: Life expectancy
Size of the bubble: population
Color: Country
As a final result we have a visualization that can be filtered by slider and multiselect widget
After creating this dashboard we deploy our Streamlit app to CapRover.