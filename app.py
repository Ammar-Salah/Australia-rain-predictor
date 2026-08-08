import streamlit as st
import datetime
from main import predict_rain

st.title("🌧️ Rain Tomorrow Predictor")
st.write("Enter weather parameters to predict if it will rain tomorrow.")

# locations and wind directions
locations = [
    "Adelaide", "Albany", "Albury", "AliceSprings", "BadgerysCreek",
    "Ballarat", "Bendigo", "Brisbane", "Cairns", "Canberra", "Cobar",
    "CoffsHarbour", "Dartmoor", "Darwin", "GoldCoast", "Hobart",
    "Katherine", "Launceston", "Melbourne", "MelbourneAirport", "Mildura",
    "Moree", "MountGambier", "MountGinini", "Newcastle", "Nhil",
    "NorahHead", "NorfolkIsland", "Nuriootpa", "PearceRAAF", "Penrith",
    "Perth", "PerthAirport", "Portland", "Richmond", "Sale", "SalmonGums",
    "Sydney", "SydneyAirport", "Townsville", "Tuggeranong", "Uluru",
    "WaggaWagga", "Walpole", "Watsonia", "Williamtown", "Witchcliffe",
    "Wollongong", "Woomera",
]

wind_directions = [
    "E", "ENE", "ESE", "N", "NE", "NNE", "NNW", "NW",
    "S", "SE", "SSE", "SSW", "SW", "W", "WNW", "WSW",
]

# date and location
st.subheader("📅 Date & Location")
col1, col2 = st.columns(2)
with col1:
    date = st.date_input("Date", value=datetime.date.today())
with col2:
    location = st.selectbox("Location", locations)

# temperature
st.subheader("🌡️ Temperature")
col1, col2, col3, col4 = st.columns(4)
with col1:
    min_temp = st.number_input("Min Temp (°C)", value=12.0)
with col2:
    max_temp = st.number_input("Max Temp (°C)", value=22.0)
with col3:
    temp_9am = st.number_input("Temp 9am (°C)", value=15.0)
with col4:
    temp_3pm = st.number_input("Temp 3pm (°C)", value=20.0)

# rainfall and sunshine
st.subheader("☀️ Rainfall & Sunshine")
col1, col2, col3, col4 = st.columns(4)
with col1:
    rainfall = st.number_input("Rainfall (mm)", value=0.0, min_value=0.0)
with col2:
    evaporation = st.number_input("Evaporation (mm)", value=5.0, min_value=0.0)
with col3:
    sunshine = st.number_input("Sunshine (hrs)", value=8.0, min_value=0.0)
with col4:
    rain_today = st.selectbox("Rain Today?", ["No", "Yes"])

# wind
st.subheader("💨 Wind")
col1, col2, col3 = st.columns(3)
with col1:
    wind_gust_dir = st.selectbox("Wind Gust Direction", wind_directions)
with col2:
    wind_dir_9am = st.selectbox("Wind Dir 9am", wind_directions)
with col3:
    wind_dir_3pm = st.selectbox("Wind Dir 3pm", wind_directions)

col1, col2, col3 = st.columns(3)
with col1:
    wind_gust_speed = st.number_input("Gust Speed (km/h)", value=40.0, min_value=0.0)
with col2:
    wind_speed_9am = st.number_input("Speed 9am (km/h)", value=15.0, min_value=0.0)
with col3:
    wind_speed_3pm = st.number_input("Speed 3pm (km/h)", value=20.0, min_value=0.0)

# humidity and pressure
st.subheader("💧 Humidity & Pressure")
col1, col2, col3, col4 = st.columns(4)
with col1:
    humidity_9am = st.number_input("Humidity 9am (%)", value=60.0, min_value=0.0, max_value=100.0)
with col2:
    humidity_3pm = st.number_input("Humidity 3pm (%)", value=40.0, min_value=0.0, max_value=100.0)
with col3:
    pressure_9am = st.number_input("Pressure 9am (hPa)", value=1015.0)
with col4:
    pressure_3pm = st.number_input("Pressure 3pm (hPa)", value=1013.0)

# cloud cover
st.subheader("☁️ Cloud Cover")
col1, col2 = st.columns(2)
with col1:
    cloud_9am = st.slider("Cloud 9am (oktas)", 0, 8, 5)
with col2:
    cloud_3pm = st.slider("Cloud 3pm (oktas)", 0, 8, 4)

# predict button
if st.button("Predict"):
    result = predict_rain(
        date=str(date),
        location=location,
        min_temp=min_temp,
        max_temp=max_temp,
        rainfall=rainfall,
        evaporation=evaporation,
        sunshine=sunshine,
        wind_gust_dir=wind_gust_dir,
        wind_gust_speed=wind_gust_speed,
        wind_dir_9am=wind_dir_9am,
        wind_dir_3pm=wind_dir_3pm,
        wind_speed_9am=wind_speed_9am,
        wind_speed_3pm=wind_speed_3pm,
        humidity_9am=humidity_9am,
        humidity_3pm=humidity_3pm,
        pressure_9am=pressure_9am,
        pressure_3pm=pressure_3pm,
        cloud_9am=float(cloud_9am),
        cloud_3pm=float(cloud_3pm),
        temp_9am=temp_9am,
        temp_3pm=temp_3pm,
        rain_today=rain_today,
    )

    if result == 1:
        st.error("🌧️ Yes — It will likely rain tomorrow!")
    else:
        st.success("☀️ No — No rain expected tomorrow!")
