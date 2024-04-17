from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

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


# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.title("Use Pygwalker In Streamlit")

# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    rental_sales = pd.read_csv('Cleaned Data/state_rentals_excluding_hawaii_alaska.csv')
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(rental_sales, spec=vis_spec, spec_io_mode="rw")


renderer = get_pyg_renderer()

st.subheader("Display Explore UI")

tab1, tab2, tab3, tab4 = st.tabs(
    ["graphic walker", "data profiling", "graphic renderer", "pure chart"]
)

with tab1:
    renderer.explorer()

with tab2:
    renderer.explorer(default_tab="data")

with tab3:
    renderer.viewer()

with tab4:
    st.markdown("### registered per weekday")
    renderer.chart(0)
    st.markdown("### registered per day")
    renderer.chart(1)