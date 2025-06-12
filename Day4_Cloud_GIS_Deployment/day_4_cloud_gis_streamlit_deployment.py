# streamlit_app.py – Geospatial Dashboard using Leafmap

import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("📍 Geospatial Dashboard – Village Boundary Viewer")

# Sidebar filter
with st.sidebar:
    st.header("Map Controls")
    show_layer = st.checkbox("Show Village Boundaries", value=True)

# Initialize map
m = leafmap.Map(center=[19.76, 75.34], zoom=6)

# Add layer
if show_layer:
    m.add_geojson("data/sample_villages.geojson", layer_name="Villages")

m.to_streamlit(height=600)
