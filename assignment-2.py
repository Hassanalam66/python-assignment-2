import streamlit as st

st.set_page_config(page_title="Simple Unit Converter", page_icon="🔄", layout="centered")

st.title("🔄 Simple Unit Converter")

# Select Unit Type
unit_type = st.selectbox("Select Unit Category", ["Length", "Weight", "Temperature", "Speed", "Time", "Volume"])

# Unit Data
conversion_data = {
    "Length": {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001},
    "Weight": {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495},
    "Speed": {"m/s": 1, "km/h": 0.277778, "mph": 0.44704, "knot": 0.514444},
    "Time": {"Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400},
    "Volume": {"Liter": 1, "Milliliter": 0.001, "Gallon": 3.78541, "Cubic Meter": 1000}
}

# Conversion Functions
def convert_temp(value, from_u, to_u):
    if from_u == "Celsius":
        return value * 9/5 + 32 if to_u == "Fahrenheit" else value + 273.15 if to_u == "Kelvin" else value
    elif from_u == "Fahrenheit":
        return (value - 32) * 5/9 if to_u == "Celsius" else ((value - 32) * 5/9) + 273.15 if to_u == "Kelvin" else value
    elif from_u == "Kelvin":
        return value - 273.15 if to_u == "Celsius" else ((value - 273.15) * 9/5) + 32 if to_u == "Fahrenheit" else value
    return value

# Input Fields
if unit_type == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
else:
    from_unit = st.selectbox("From", list(conversion_data[unit_type].keys()))
    to_unit = st.selectbox("To", list(conversion_data[unit_type].keys()))

value = st.number_input("Enter Value", format="%.2f")

# Conversion Logic
if st.button("Convert"):
    if unit_type == "Temperature":
        result = convert_temp(value, from_unit, to_unit)
    else:
        result = value * (conversion_data[unit_type][to_unit] / conversion_data[unit_type][from_unit])
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
