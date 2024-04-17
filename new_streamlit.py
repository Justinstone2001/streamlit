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

logo_path = "zillow.png"

# Display the logo at the top left

st.image(logo_path, width=50)

    
# Inject custom CSS styles
st.markdown("""
<style>
body {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
h1 {
    color: #0b4f6c;
    background-color: #f0f0f0; /* Light grey background */
    padding: 20px; /* Adds space around the text inside the h1 element */
    border-radius: 10px; /* Rounds the corners */
    margin: 20px 0; /* Adds space above and below the h1 element, keeping it centered */
}

h2 {
    color: #01baef;
    background-color: #f0f0f0; /* Light grey background */
    padding: 15px; /* Adds space around the text inside the h2 element */
    border-radius: 10px; /* Rounds the corners */
    margin: 15px 0; /* Adds space above and below the h2 element */
}

div.stButton > button:first-child {
    background-color: #f0f0f0; /* Light grey background */
    color: #ffffff; /* White text color */
    border-radius: 5px; /* Rounded corners for the button */
    padding: 10px 20px; /* Horizontal and vertical padding */
}

</style>
""", unsafe_allow_html=True)

# Main Title
st.title("Zillow Data Analysis Dashboard")

# Dashboard Introduction
st.markdown("""
This dashboard provides a visual analysis of rental and sales data from Zillow, focusing on major metropolitan areas and median sales prices across the United States. Scroll down to explore different visualizations and insights.
""")

# Interactive Geo-Spatial Analysis Section
st.header("Interactive Geo-Spatial Analysis")
st.markdown("Explore the interactive maps below, showing detailed information on rental and median sales data across different regions.")

# Renderer setup
@st.cache_resource
def get_pyg_renderer(data_path: str, spec_path: str) -> "StreamlitRenderer":
    data = pd.read_csv(data_path)
    return StreamlitRenderer(data, spec=spec_path, debug=False)

# Rental and sales price renderers
renderer = get_pyg_renderer("Cleaned Data/state_rentals_excluding_hawaii_alaska.csv", "rentals.json")
renderer2 = get_pyg_renderer("Cleaned Data/median_sales_excluding_hawaii_alaska.csv", "median.json")

# Tabbed plots for different data sets
tab1, tab2 = st.tabs(["Rental Prices", "Sales Prices"])
with tab1:
    renderer.chart(0)
with tab2:
    renderer2.chart(0)

# Monthly rent trends section
st.header("Trend of Monthly Rent Prices for Selected Major Metro Areas")
st.markdown("The following line graph displays trends in monthly rent prices over time for selected major metropolitan areas.")

# Plotting rental trends
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
 
# Streamlit interface
df = predicted_sales
df['Base Date Recorded'] = pd.to_datetime(df['Base Date Recorded'])
df['Forecast Date'] = pd.to_datetime(df['Forecast Date'])

st.title("Zillow Data Analysis Dashboard")

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