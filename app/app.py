import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Gapminder')
st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")
@st.cache_data
def load_data():

    df_pop = pd.read_csv("data/pop.csv").dropna(how='all')
    df_lex = pd.read_csv("data/lex.csv").dropna(how='all')
    df_gdp = pd.read_csv("data/gni.csv").dropna(how='all')
    
    df_pop_filled = df_pop.fillna(method='ffill')
    df_lex_filled = df_lex.fillna(method='ffill')
    df_gdp_filled = df_gdp.fillna(method='ffill')

    df_pop_tidy = pd.melt(df_pop_filled, id_vars=['country'], var_name='year', value_name='population')
    df_lex_tidy = pd.melt(df_lex_filled, id_vars=['country'], var_name='year', value_name='life_expectancy')
    df_gdp_tidy = pd.melt(df_gdp_filled, id_vars=['country'], var_name='year', value_name='gni_per_capita')
    merged_df = pd.merge(df_pop_tidy, df_lex_tidy, on=['country', 'year'])
    merged_df = pd.merge(merged_df, df_gdp_tidy, on=['country', 'year'])
    
    return merged_df

merged_df = load_data()
st.write("Merged Data first 5 columns:")
st.write(merged_df.head())
merged_df = merged_df[merged_df['gni_per_capita'] > 0]
min_year = int(merged_df["year"].min())
max_year = int(merged_df["year"].max())

if 'slider' not in st.session_state:
  st.session_state['slider'] = min_year
selected_year = st.sidebar.slider("Select Year:", min_value=min_year, max_value=max_year, value=st.session_state['slider'], key="year_slider")
selected_countries = st.multiselect("Select Countries:", merged_df["country"].unique(), key="country_multiselect")
filtered_df = merged_df[merged_df["year"] == str(selected_year)]
if selected_countries:
    filtered_df = filtered_df[filtered_df["country"].isin(selected_countries)]

fig = px.scatter(
    filtered_df,
    x="gni_per_capita",
    y="life_expectancy",
    size="population",
    color="country",
    log_x=True,  
    range_x=[merged_df['gni_per_capita'].min(), merged_df['gni_per_capita'].max()]
)

fig.update_layout(
    title="Gapminder: Life Expectancy vs. GNI per Capita",
    xaxis_title="Logarithmic GNI per Capita (PPP)",
    yaxis_title="Life Expectancy",
)

st.plotly_chart(fig)
