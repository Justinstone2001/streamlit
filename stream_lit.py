import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import matplotlib.pyplot as plt


# Paste the copied Pygwalker chart code here
vis_spec = """[
  {
    "config": {
      "defaultAggregated": true,
      "geoms": [
        "poi"
      ],
      "coordSystem": "geographic",
      "limit": -1,
      "timezoneDisplayOffset": 0
    },
    "encodings": {
      "dimensions": [
        {
          "dragId": "gw_dOue",
          "fid": "Region Name",
          "name": "Region Name",
          "basename": "Region Name",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_C3og",
          "fid": "Region Type",
          "name": "Region Type",
          "basename": "Region Type",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_Z_gj",
          "fid": "State Name",
          "name": "State Name",
          "basename": "State Name",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_KZ6B",
          "fid": "Date Recorded",
          "name": "Date Recorded",
          "basename": "Date Recorded",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_hpco",
          "fid": "Coordinates",
          "name": "Coordinates",
          "basename": "Coordinates",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_ngIl",
          "fid": "Latitude",
          "name": "Latitude",
          "basename": "Latitude",
          "semanticType": "quantitative",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_Zf19",
          "fid": "Longitude",
          "name": "Longitude",
          "basename": "Longitude",
          "semanticType": "quantitative",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_mea_key_fid",
          "fid": "gw_mea_key_fid",
          "name": "Measure names",
          "analyticType": "dimension",
          "semanticType": "nominal"
        },
        {
          "fid": "Coordinates_x",
          "name": "Coordinates_x",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "basename": "Coordinates_x",
          "dragId": "GW_VYCpk5ED"
        },
        {
          "fid": "Coordinates_y",
          "name": "Coordinates_y",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "basename": "Coordinates_y",
          "dragId": "GW_JKRPZtl7"
        }
      ],
      "measures": [
        {
          "dragId": "gw_MYF3",
          "fid": "RegionID",
          "name": "RegionID",
          "basename": "RegionID",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum",
          "offset": 0
        },
        {
          "dragId": "gw_-Y8K",
          "fid": "SizeRank",
          "name": "SizeRank",
          "basename": "SizeRank",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum",
          "offset": 0
        },
        {
          "dragId": "gw_r6fq",
          "fid": "Monthly Rent",
          "name": "Monthly Rent",
          "basename": "Monthly Rent",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum",
          "offset": 0
        },
        {
          "dragId": "gw_count_fid",
          "fid": "gw_count_fid",
          "name": "Row count",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum",
          "computed": true,
          "expression": {
            "op": "one",
            "params": [],
            "as": "gw_count_fid"
          }
        },
        {
          "dragId": "gw_mea_val_fid",
          "fid": "gw_mea_val_fid",
          "name": "Measure values",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "sum"
        },
        {
          "fid": "Latitude_x",
          "name": "Latitude_x",
          "semanticType": "quantitative",
          "analyticType": "measure",
          "basename": "Latitude_x",
          "dragId": "GW_qaPKwEiy"
        },
        {
          "fid": "Longitude_x",
          "name": "Longitude_x",
          "semanticType": "quantitative",
          "analyticType": "measure",
          "basename": "Longitude_x",
          "dragId": "GW_cO9otU5l"
        },
        {
          "fid": "Latitude_y",
          "name": "Latitude_y",
          "semanticType": "quantitative",
          "analyticType": "measure",
          "basename": "Latitude_y",
          "dragId": "GW_g9hY6ZRz"
        },
        {
          "fid": "Longitude_y",
          "name": "Longitude_y",
          "semanticType": "quantitative",
          "analyticType": "measure",
          "basename": "Longitude_y",
          "dragId": "GW_M3jWtosp"
        }
      ],
      "rows": [],
      "columns": [],
      "color": [
        {
          "dragId": "gw_nFfb",
          "fid": "Monthly Rent",
          "name": "Monthly Rent",
          "basename": "Monthly Rent",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "mean",
          "offset": 0
        }
      ],
      "opacity": [],
      "size": [
        {
          "dragId": "gw_gdUr",
          "fid": "Monthly Rent",
          "name": "Monthly Rent",
          "basename": "Monthly Rent",
          "analyticType": "measure",
          "semanticType": "quantitative",
          "aggName": "mean",
          "offset": 0
        }
      ],
      "shape": [],
      "radius": [],
      "theta": [],
      "longitude": [
        {
          "dragId": "gw_EXfj",
          "fid": "Longitude",
          "name": "Longitude",
          "basename": "Longitude",
          "semanticType": "quantitative",
          "analyticType": "dimension",
          "offset": 0
        }
      ],
      "latitude": [
        {
          "dragId": "gw_lgVz",
          "fid": "Latitude",
          "name": "Latitude",
          "basename": "Latitude",
          "semanticType": "quantitative",
          "analyticType": "dimension",
          "offset": 0
        }
      ],
      "geoId": [],
      "details": [
        {
          "dragId": "gw_qtvl",
          "fid": "Date Recorded",
          "name": "Date Recorded",
          "basename": "Date Recorded",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        },
        {
          "dragId": "gw_Xulw",
          "fid": "State Name",
          "name": "State Name",
          "basename": "State Name",
          "semanticType": "nominal",
          "analyticType": "dimension",
          "offset": 0
        }
      ],
      "filters": [],
      "text": []
    },
    "layout": {
      "showActions": false,
      "showTableSummary": false,
      "stack": "stack",
      "interactiveScale": false,
      "zeroScale": true,
      "background": "",
      "size": {
        "mode": "auto",
        "width": 800,
        "height": 600
      },
      "format": {},
      "geoKey": "name",
      "resolve": {
        "x": false,
        "y": false,
        "color": false,
        "opacity": false,
        "shape": false,
        "size": false
      },
      "scaleIncludeUnmatchedChoropleth": false,
      "colorPalette": "reds",
      "useSvg": false,
      "scale": {
        "opacity": {},
        "size": {}
      },
      "geoMapTileUrl": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    },
    "visId": "gw_LtRJ",
    "name": "Chart 1"
  }
]"""

 
vis_spec2 = r"""{"config":[{"config":{"defaultAggregated":true,"geoms":["poi"],"coordSystem":"geographic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"dragId":"gw_qv1d","fid":"Region Name","name":"Region Name","basename":"Region Name","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_i0lF","fid":"Region Type","name":"Region Type","basename":"Region Type","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_nd02","fid":"State Name","name":"State Name","basename":"State Name","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_uVME","fid":"Date Recorded","name":"Date Recorded","basename":"Date Recorded","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_ZhK_","fid":"Coordinates","name":"Coordinates","basename":"Coordinates","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_Lo9v","fid":"Latitude","name":"Latitude","basename":"Latitude","semanticType":"quantitative","analyticType":"dimension","offset":0},{"dragId":"gw_mHJy","fid":"Longitude","name":"Longitude","basename":"Longitude","semanticType":"quantitative","analyticType":"dimension","offset":0},{"dragId":"gw_mea_key_fid","fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"dragId":"gw_w6tJ","fid":"RegionID","name":"RegionID","basename":"RegionID","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"dragId":"gw_8hZM","fid":"SizeRank","name":"SizeRank","basename":"SizeRank","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"dragId":"gw_SKPZ","fid":"Median Sale Price","name":"Median Sale Price","basename":"Median Sale Price","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"dragId":"gw_count_fid","fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"dragId":"gw_mea_val_fid","fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[],"columns":[],"color":[{"dragId":"gw_m3ce","fid":"Median Sale Price","name":"Median Sale Price","basename":"Median Sale Price","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0}],"opacity":[],"size":[{"dragId":"gw_6wO4","fid":"Median Sale Price","name":"Median Sale Price","basename":"Median Sale Price","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0}],"shape":[],"radius":[],"theta":[],"longitude":[{"dragId":"gw__Ohq","fid":"Longitude","name":"Longitude","basename":"Longitude","semanticType":"quantitative","analyticType":"dimension","offset":0}],"latitude":[{"dragId":"gw_QVWO","fid":"Latitude","name":"Latitude","basename":"Latitude","semanticType":"quantitative","analyticType":"dimension","offset":0}],"geoId":[],"details":[{"dragId":"gw_aCNW","fid":"Date Recorded","name":"Date Recorded","basename":"Date Recorded","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_mnn_","fid":"State Name","name":"State Name","basename":"State Name","semanticType":"nominal","analyticType":"dimension","offset":0}],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"auto","width":800,"height":600},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false},"scaleIncludeUnmatchedChoropleth":false,"colorPalette":"reds","useSvg":false,"scale":{"opacity":{},"size":{}}},"visId":"gw_XwBR","name":"Chart 1"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"view","query":[{"op":"aggregate","groupBy":["Longitude","Latitude","Date Recorded","State Name"],"measures":[{"field":"Median Sale Price","agg":"mean","asFieldKey":"Median Sale Price_mean"}]}]}]}],"version":"0.4.7"}"""


vis_spec3 = r"""{"config":[{"config":{"defaultAggregated":true,"geoms":["auto"],"coordSystem":"generic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"dragId":"gw_mL1e","fid":"Region Name","name":"Region Name","basename":"Region Name","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_D8IG","fid":"Region Type","name":"Region Type","basename":"Region Type","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_bLDN","fid":"State Name","name":"State Name","basename":"State Name","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_Vg4G","fid":"Date Recorded","name":"Date Recorded","basename":"Date Recorded","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_a8mH","fid":"Coordinates","name":"Coordinates","basename":"Coordinates","semanticType":"nominal","analyticType":"dimension","offset":0},{"dragId":"gw_5r1K","fid":"Latitude","name":"Latitude","basename":"Latitude","semanticType":"quantitative","analyticType":"dimension","offset":0},{"dragId":"gw_ZJD-","fid":"Longitude","name":"Longitude","basename":"Longitude","semanticType":"quantitative","analyticType":"dimension","offset":0},{"dragId":"gw_mea_key_fid","fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"dragId":"gw_WSqI","fid":"RegionID","name":"RegionID","basename":"RegionID","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"dragId":"gw_wXRU","fid":"SizeRank","name":"SizeRank","basename":"SizeRank","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"dragId":"gw_RdCr","fid":"Median Sale Price","name":"Median Sale Price","basename":"Median Sale Price","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"dragId":"gw_count_fid","fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"dragId":"gw_mea_val_fid","fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"dragId":"gw_mR9g","fid":"Median Sale Price","name":"Median Sale Price","basename":"Median Sale Price","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0}],"columns":[{"dragId":"gw_ebdP","fid":"State Name","name":"State Name","basename":"State Name","semanticType":"nominal","analyticType":"dimension","offset":0,"sort":"descending"}],"color":[{"dragId":"gw_OiaK","fid":"Median Sale Price","name":"Median Sale Price","basename":"Median Sale Price","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"fixed","height":372,"width":689},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false},"scaleIncludeUnmatchedChoropleth":false,"colorPalette":"reds","useSvg":false,"scale":{"opacity":{},"size":{}}},"visId":"gw_oTUm","name":"Chart 1"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"view","query":[{"op":"aggregate","groupBy":["State Name"],"measures":[{"field":"Median Sale Price","agg":"mean","asFieldKey":"Median Sale Price_mean"}]}]}]}],"version":"0.4.7"}"""


# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Zillow Data Analysis",
    layout="wide"
)

# Main title
st.title("Zillow Data Analysis Dashboard")

# Introduction or explanation of the dashboard
st.markdown("""
This dashboard provides a visual analysis of rental and sales data from Zillow, focusing on major metropolitan areas and median sales prices across the United States. Scroll down to explore different visualizations and insights.
""")

# Section header for the rental trends graph
st.header("Trend of Monthly Rent Prices for Selected Major Metro Areas")
st.markdown("""
The following line graph displays trends in monthly rent prices over time for selected major metropolitan areas.
""")

# Import your data
rental_sales = pd.read_csv('Cleaned Data/state_rentals_excluding_hawaii_alaska.csv')
median_sales = pd.read_csv('Cleaned Data/median_sales_excluding_hawaii_alaska.csv')
rental_sales['Date Recorded'] = pd.to_datetime(rental_sales['Date Recorded'])

# Plot for rental trends
all_cities = rental_sales['Region Name'].unique()

# User selection of cities
selected_cities = st.multiselect('Select Cities', all_cities, default=['New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Dallas, TX', 'San Francisco, CA'])
filtered_rentals = rental_sales[rental_sales['Region Name'].isin(selected_cities)]

# Plotting the data
if not filtered_rentals.empty:
    plt.figure(figsize=(8, 3))
    for city in selected_cities:
        city_data = filtered_rentals[filtered_rentals['Region Name'] == city]
        if not city_data.empty:
            plt.plot(city_data['Date Recorded'], city_data['Monthly Rent'], label=city)
    plt.title('Trend of Monthly Rent Prices for Selected Major Metro Areas')
    plt.xlabel('Year')
    plt.ylabel('Monthly Rent ($)')
    plt.legend(title='Metro Area')
    plt.grid(True)
    st.pyplot(plt)
else:
    st.write("No data available for the selected cities.")

# Section header for Pygwalker visualization
st.header("Interactive Geo-Spatial Analysis")
st.markdown("""
Explore the interactive maps below, showing detailed information on rental and median sales data across different regions.
""")

# Pygwalker visualizations
pyg_html_rental = pyg.to_html(rental_sales, spec=vis_spec)
pyg_html_median = pyg.to_html(median_sales, spec=vis_spec2)
pyg_html_graph = pyg.to_html(median_sales, spec=vis_spec3)

components.html(pyg_html_graph, height=800, scrolling=True)
components.html(pyg_html_rental, height=800, scrolling=True)
components.html(pyg_html_median, height=800, scrolling=True)


# # Using columns to place the Pygwalker charts side by side
# col1, col2= st.columns(2)
# with col1:
#     st.subheader("Average Rent Prices by State")
#     components.html(pyg_html_rental, height=800, scrolling=True)
# with col2:
#     st.subheader("Median Sales Prices by State ")
#     components.html(pyg_html_median, height=800, scrolling=True)



