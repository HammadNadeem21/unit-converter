import streamlit as st

st.set_page_config(page_title="Unit-Converter")

# CSS Injection
st.markdown(
    """
    <style>
        div[data-baseweb="select"] {
            cursor: pointer !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔄 Unit Converter")
st.write("Convert different units easily!")

# Units
units = [
    "Length",
    "Data Transfer Rate",
    "Digital Storage",
    "Energy",
    "Frequency",
    "Fuel Economy",
    "Area",
    "Mass",
    "Plane Angle",
    "Pressure",
    "Speed",
    "Tempreture",
    "Time",
    "Volume"
]
selected_unit = st.selectbox("Select Unit", units)


# selected unit
# st.subheader("📏 Length Converter")
st.subheader(f"{selected_unit}")
length_units = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Centimeters": 100,
    "Millimeters": 1000,
    "Miles": 0.000621371,
    "Yards": 1.09361,
    "Feet": 3.28084,
    "Inches": 39.3701
}

amount = st.number_input("Enter Value:", min_value=0.0, value=None, format="%.2f")
from_unit = st.selectbox("From", list(length_units.keys()))