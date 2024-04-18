from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pygwalker as pyg
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Read and preprocess data
rental_sales = pd.read_csv("Cleaned Data/state_rentals_excluding_hawaii_alaska.csv")
rental_sales['Date Recorded'] = pd.to_datetime(rental_sales['Date Recorded'])
median_sales = pd.read_csv('Cleaned Data/median_sales_excluding_hawaii_alaska.csv')
predicted_sales = pd.read_csv('Cleaned Data/cleaned_state_home_forecast.csv')

# Streamlit page configuration
st.set_page_config(page_title="Zillow Data Analysis", layout="wide", page_icon="zillow.png")
init_streamlit_comm()

# LOGO
logo_path = "zillow.png"
st.image(logo_path, width=50)

# Custom CSS 
st.markdown("""
<style>
body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}
h1 {
    color: #0b4f6c;
    background-color: #f0f0f0;
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0;
}
h2 {
    color: #01baef;
    background-color: #f0f0f0;
    padding: 15px;
    border-radius: 10px;
    margin: 15px 0;
}
div.stButton > button:first-child {
    background-color: #f0f0f0;
    color: #ffffff;
    border-radius: 5px;
    padding: 10px 20px;
}
div.streamlit-container {
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# Main Title
st.title("Zillow Data Analysis Dashboard")

# Dashboard Introduction
st.markdown("This dashboard provides a visual analysis of rental and sales data from Zillow. Scroll down to explore different visualizations and insights.")

# Renderer setup
@st.cache_resource
def get_pyg_renderer(data_path: str, spec_path: str) -> "StreamlitRenderer":
    data = pd.read_csv(data_path)
    return StreamlitRenderer(data, spec=spec_path, debug=False)

# Rental and sales price renderers
renderer = get_pyg_renderer("Cleaned Data/2023_rental_price.csv", "rentals_2023.json")
renderer2 = get_pyg_renderer("Cleaned Data/2023_sales_state.csv", "median_sales_2023.json")
renderer3 = get_pyg_renderer("Cleaned Data/2023_sale_price.csv", "geographic_2023_sales.json")

# Tabbed plots 
tab1, tab2, tab3 = st.tabs(["Rental Prices", "Sales Prices", "2023 Prices by City"])
with tab1:
    st.header("State-Wide Median Rent Price Averages in 2023")
    renderer.chart(0)
with tab2:
    st.header("State-Wide Median Sale Price Averages in 2023")
    renderer2.chart(0)
with tab3:
    st.header("City-Wide Median Sale Price Averages in 2023")
    renderer3.chart(0)


# Plotting rental trends
st.header("Interactive Rental Trends")

all_cities = rental_sales['Region Name'].unique()
selected_cities = st.multiselect('Select Cities', all_cities, default=['New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Dallas, TX', 'San Francisco, CA'])
filtered_rentals = rental_sales[rental_sales['Region Name'].isin(selected_cities)]

if not filtered_rentals.empty:
    plt.figure(figsize=(8, 3))  # Adjust size as needed
    for city in selected_cities:
        city_data = filtered_rentals[filtered_rentals['Region Name'] == city]
        plt.plot(city_data['Date Recorded'], city_data['Monthly Rent'], label=city)
    plt.title('Trend of Monthly Rent Prices for Selected Major Metro Areas')
    plt.xlabel('Year')
    plt.ylabel('Monthly Rent ($)')
    # Position the legend outside of the plot
    plt.legend(title='Metro Area', loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.tight_layout()  # This can help to fit everything within the figure cleanly
    st.pyplot(plt)
else:
    st.write("No data available for the selected cities.")


# Predicted Sales Calculator
df = predicted_sales
df['Base Date Recorded'] = pd.to_datetime(df['Base Date Recorded'])
df['Forecast Date'] = pd.to_datetime(df['Forecast Date'])

st.title("Forecasted Growth Finder")
st.markdown("Forecast Growht % represents the projected percentage change in home values")
# User input for selecting a state
selected_state = st.selectbox('Select State', df['State Name'].unique())

# Filter data based on the selected state
state_data = df[df['State Name'] == selected_state]

# User input for selecting a city from the filtered state data
if not state_data.empty:
    selected_city = st.selectbox('Select City', state_data['Region Name'].unique())

    # Filter city data based on the selected city
    city_data = state_data[state_data['Region Name'] == selected_city]

    # Display the data using HTML
    if not city_data.empty:
        st.markdown("### Forecast Growth (%) for selected city:")
        html = city_data[['Region Name', 'Forecast Date', 'Forecast Growth (%)']].to_html(index=False)
        st.write(html, unsafe_allow_html=True)
    else:
        st.write("No data available for the selected city.")
else:
    st.write("No data available for the selected state.")
