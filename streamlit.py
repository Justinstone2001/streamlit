from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pygwalker as pyg
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Read and preprocess data
csv_path = os.path.abspath("Cleaned_Data/state_rentals_excluding_hawaii_alaska.csv")

rental_sales = pd.read_csv(csv_path)
rental_sales['Date Recorded'] = pd.to_datetime(rental_sales['Date Recorded'])
median_sales = pd.read_csv('Cleaned_Data/median_sales_excluding_hawaii_alaska.csv')
predicted_sales = pd.read_csv('Cleaned_Data/cleaned_state_home_forecast.csv')

# Streamlit page configuration
st.set_page_config(page_title="Zillow Data Analysis", layout="wide", page_icon="zillow.png")
init_streamlit_comm()

# LOGO
logo_path = "Pictures/zillow.png"
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
renderer = get_pyg_renderer("Cleaned_Data/2023_rental_price.csv", "Json/rentals_2023.json")
renderer2 = get_pyg_renderer("Cleaned_Data/2023_sales_state.csv", "Json/median_sales_2023.json")
renderer3 = get_pyg_renderer("Cleaned_Data/2023_sale_price.csv", "Json/geographic_2023_sales.json")
renderer4 = get_pyg_renderer("Cleaned_Data/2023_rental_price_city.csv", "Json/rental_city_2023.json")

# Tabbed plots 
tab1, tab2, tab3, tab4 = st.tabs(["Monthly Rent by State", "Housing Prices by State", "Housing Prices by City", "Monthly Rent by City"])
with tab1:
    st.header("State-Wide Median Rent Price Averages in 2023")
    renderer.chart(0)
with tab2:
    st.header("State-Wide Median Sale Price Averages in 2023")
    renderer2.chart(0)
with tab3:
    st.header("City-Wide Median Sale Price Averages in 2023")
    renderer3.chart(0)
with tab4:
    st.header("City-Wide Median Montlhy Rent Averages in 2023")
    renderer4.chart(0)


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


# Forecasted Sales Visualization 
df = predicted_sales
df['Base Date Recorded'] = pd.to_datetime(df['Base Date Recorded'])
df['Forecast Date'] = pd.to_datetime(df['Forecast Date'])

st.header("Forecasted Growth Finder")
st.markdown("Forecast Growth % represents the projected percentage change in home values")
# User input for selecting a state
selected_state = st.selectbox('Select State', df['State Name'].unique())

# Filter data based on the selected state
state_data = df[df['State Name'] == selected_state]

# User input for selecting a city from the filtered state data
if not state_data.empty:
    selected_city = st.selectbox('Select City', state_data['Region Name'].unique())

    # Filter city data based on the selected city
    city_data = state_data[state_data['Region Name'] == selected_city]

    if not city_data.empty:
        st.markdown("### Forecast Growth (%) for selected city:")
        # Set seaborn style
        sns.set(style="whitegrid")
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plotting
        sns.lineplot(data=city_data, x='Forecast Date', y='Forecast Growth (%)', marker='o', ax=ax)
        ax.set_xlabel('Forecast Date')
        ax.set_ylabel('Forecast Growth (%)')
        ax.set_title('Forecasted Growth Trend')
        plt.xticks(rotation=45)  
        plt.tight_layout()  # Adjust layout for better spacing

        st.pyplot(fig)
    else:
        st.write("No data available for the selected city.")
else:
    st.write("No data available for the selected state.")
    
    
# Morgage Visualization
rental_data = pd.read_csv('Cleaned_Data/cleaned_state_rentals.csv')
median_sales_data = pd.read_csv('Cleaned_Data/cleaned_median_sales.csv')

# Define the mortgage calculation function
def calculate_monthly_mortgage(median_price):
    down_payment_percentage = 0.20
    loan_amount = median_price * (1 - down_payment_percentage)
    annual_interest_rate = 0.0711  # 7.11% interest rate
    mortgage_term_years = 30

    monthly_interest_rate = annual_interest_rate / 12
    total_payments = mortgage_term_years * 12

    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                      ((1 + monthly_interest_rate) ** total_payments - 1)

    return monthly_payment

# Calculate the average rent for each region
average_rent_by_region = rental_data.groupby('Region Name')['Monthly Rent'].mean().reset_index()

# Merge rental data with median sales price data
rent_vs_sales = pd.merge(average_rent_by_region, median_sales_data, on='Region Name')

# Calculate the monthly mortgage payment for each region
rent_vs_sales['Monthly Mortgage'] = rent_vs_sales['Median Sale Price'].apply(calculate_monthly_mortgage)

# Calculate the mean monthly mortgage across all regions
mean_monthly_mortgage = rent_vs_sales['Monthly Mortgage'].mean()

# Function to plot the line chart
def plot_line_chart(selected_state, selected_city):
    city_data = rent_vs_sales[(rent_vs_sales['State Name'] == selected_state) & (rent_vs_sales['Region Name'] == selected_city)]

    if city_data.empty:
        st.write("No data available for the selected city.")
        return

    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotting
    ax.plot(city_data['Region Name'], city_data['Monthly Rent'], marker='o', markersize=12, label='Monthly Rent', color='blue')
    ax.plot(city_data['Region Name'], city_data['Monthly Mortgage'], marker='s', label='Monthly Mortgage', color='red')
    ax.axhline(y=mean_monthly_mortgage, color='green', linestyle='--', label=f'Mean Monthly Mortgage (${mean_monthly_mortgage:.2f})')
    ax.set_title(f'Rent vs Mortgage Payment in {selected_city}, {selected_state}')
    ax.set_xlabel('Region Name')
    ax.set_ylabel('Amount ($)')
    ax.legend()
    ax.grid(True)
    ax.set_xticklabels(city_data['Region Name'], rotation=45)
    plt.tight_layout()

    st.pyplot(fig)  # Show the plot using Streamlit

# Streamlit app
st.header("Rent vs Mortgage Payment")
st.markdown("Compare average monthly rent with average monthly mortgage payment for selected city and state")

# User input for selecting a state
selected_state = st.selectbox('Select State', rent_vs_sales['State Name'].unique())

# Filter cities based on the selected state
cities_in_state = rent_vs_sales[rent_vs_sales['State Name'] == selected_state]['Region Name'].unique()

# User input for selecting a city from the filtered state data
selected_city = st.selectbox('Select City', cities_in_state)

# Plot the line chart for the selected city and state
plot_line_chart(selected_state, selected_city)