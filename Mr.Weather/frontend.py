import streamlit as st
from open_api import get_hourly_data
from utils import get_location
params = {
	"latitude": 48.8534,
	"longitude": 2.3488,
	"hourly": ["temperature_2m", "precipitation_probability", "snowfall", "visibility", "wind_speed_10m"],
	"start_date": "2024-03-14",
	"end_date": "2024-03-14"
}

st.title("Mr.Weather")
# col_1, col_2 = st.columns(2)

# with col_1:
#     city = st.text_input('City', 'Paris')
# with col_2:
#     btn = st.button('Fetch')

city = st.text_input('City', 'Paris')
btn = st.button('Fetch')
if btn:
    geo_coord = get_location(city)
    params['latitude'] = float(geo_coord.lat)
    params['longitude'] = float(geo_coord.lon)
    data = get_hourly_data(params)
    st.dataframe(data)
