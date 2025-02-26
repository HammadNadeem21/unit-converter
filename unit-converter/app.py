import streamlit as st

# Page Configurations
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS Styling (Light Mode Optimized)
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
           
        }
        .stApp {
          
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 8px 16px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        div[data-baseweb="select"] {
            cursor: pointer !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🔄 Unit Converter")
st.write("Easily convert different units in one place!")

# Units Dictionary
units_dict = {
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701
    },
    "Mass": {
        "Grams": 1,
        "Kilograms": 0.001,
        "Milligrams": 1000,
        "Micrograms": 1000000,
        "Pounds": 0.00220462,
        "Ounces": 0.035274,
        "Stones": 0.000157473,
        "Tonnes": 0.000001
    },
    "Speed": {
        "Meters per second": 1,
        "Kilometers per hour": 3.6,
        "Miles per hour": 2.23694,
        "Feet per second": 3.28084,
        "Knots": 1.94384
    },
    "Area": {
        "Square Meters": 1,
        "Square Kilometers": 0.000001,
        "Square Centimeters": 10000,
        "Square Millimeters": 1000000,
        "Hectares": 0.0001,
        "Acres": 0.000247105,
        "Square Miles": 3.861e-7,
        "Square Yards": 1.19599,
        "Square Feet": 10.7639,
        "Square Inches": 1550.0031
    },
    "Energy": {
        "Joules": 1,
        "Kilojoules": 0.001,
        "Calories": 0.239006,
        "Kilocalories": 0.000239006,
        "Watt-hours": 0.000277778,
        "Kilowatt-hours": 2.7778e-7,
        "Electronvolts": 6.242e+18,
        "British Thermal Units": 0.000947817
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 0.001,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9
    },
    "Data Transfer Rate": {
        "Bits per second": 1,
        "Kilobits per second": 0.001,
        "Megabits per second": 1e-6,
        "Gigabits per second": 1e-9,
        "Terabits per second": 1e-12,
        "Bytes per second": 0.125,
        "Kilobytes per second": 0.000125,
        "Megabytes per second": 1.25e-7,
        "Gigabytes per second": 1.25e-10,
        "Terabytes per second": 1.25e-13
    },
    "Digital Storage": {
        "Bits": 1,
        "Bytes": 0.125,
        "Kilobits": 0.001,
        "Kilobytes": 0.000125,
        "Megabits": 1e-6,
        "Megabytes": 1.25e-7,
        "Gigabits": 1e-9,
        "Gigabytes": 1.25e-10,
        "Terabits": 1e-12,
        "Terabytes": 1.25e-13,
        "Petabytes": 1.25e-16
    },
    "Fuel Economy": {
        "Kilometers per Liter": 1,
        "Liters per 100 Kilometers": 100,
        "Miles per Gallon (US)": 2.35215,
        "Miles per Gallon (UK)": 2.82481
    },
    "Plane Angle": {
        "Degrees": 1,
        "Radians": 0.0174533,
        "Gradians": 1.11111,
        "Minutes of Arc": 60,
        "Seconds of Arc": 3600
    },
    "Pressure": {
        "Pascals": 1,
        "Kilopascals": 0.001,
        "Bars": 1e-5,
        "Atmospheres": 9.8692e-6,
        "Pounds per Square Inch": 0.000145038,
        "Millimeters of Mercury": 0.00750062
    },
"Temperature": {
    "Celsius": lambda c: c,  # Identity function (Celsius to Celsius)
    "Fahrenheit": lambda c: (c * 9/5) + 32,  # Celsius to Fahrenheit
    "Kelvin": lambda c: c + 273.15,  # Celsius to Kelvin
    "Celsius from Fahrenheit": lambda f: (f - 32) * 5/9,  # Fahrenheit to Celsius
    "Celsius from Kelvin": lambda k: k - 273.15  # Kelvin to Celsius
},
    "Time": {
        "Seconds": 1,
        "Minutes": 0.0166667,
        "Hours": 0.000277778,
        "Days": 1.1574e-5,
        "Weeks": 1.6534e-6,
        "Months": 3.8052e-7,
        "Years": 3.171e-8
    },
    "Volume": {
        "Cubic Meters": 1,
        "Cubic Centimeters": 1000000,
        "Liters": 1000,
        "Milliliters": 1000000,
        "Cubic Inches": 61023.7,
        "Cubic Feet": 35.3147,
        "Cubic Yards": 1.30795,
        "Gallons (US)": 264.172,
        "Gallons (UK)": 219.969
    }
}


# Select category
selected_unit = st.selectbox("Select Unit Type", list(units_dict.keys()))

# Selected unit
unit_options = units_dict[selected_unit]

# Input values
amount = st.number_input("Enter Value", min_value=0.0, format="%.2f")


# Filter only valid units for dropdown
valid_units = [unit for unit in unit_options.keys() if "from" not in unit]

# Select "From" and "To" units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", valid_units)
with col2:
    to_unit = st.selectbox("To", valid_units)

# Auto conversion logic
if from_unit and to_unit:
    if selected_unit == "Temperature":
        if from_unit == "Celsius":
            result = unit_options[to_unit](amount)
        elif from_unit == "Fahrenheit":
            celsius_value = unit_options["Celsius from Fahrenheit"](amount)
            result = unit_options[to_unit](celsius_value) if to_unit != "Celsius" else celsius_value
        elif from_unit == "Kelvin":
            celsius_value = unit_options["Celsius from Kelvin"](amount)
            result = unit_options[to_unit](celsius_value) if to_unit != "Celsius" else celsius_value
    else:
        result = amount * (unit_options[to_unit] / unit_options[from_unit])

    st.success(f"✅ {amount} {from_unit} = {result:.3f} {to_unit}")
