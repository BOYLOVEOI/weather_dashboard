# Import statements
import streamlit as st
import plotly.express as px
from backend import get_data

# Creating title for the web app
st.title("Weather Forecast For The Next Days")
# Creating text input widget and storing its value in city variable
city = st.text_input(label="City:")
# Creating text input widget and storing its value in country variable
country = st.text_input(label="Country Code:")
# Creating slider to determine # of days and storing its value in days variable
days = st.slider(label="Forecast Days", min_value=1, max_value=5, 
                help= "Select the number of forecasted days")
# Creating drop down option menu and storing its value in option variable
option = st.selectbox(label="Select data to view", options=("Temperature", 
                     "Sky"))
# Creating subheader for graph
st.subheader(f"{option} for the next {days} days in {city}, {country}")

# If user enters in a place, retrieve data
if city and country:
    # Call the get_data method to retrieve filtered list from OpenWeatherAPI
    data = get_data(city, country, days)

    # If user selects temperature option
    if option == 'Temperature':
        # Filter only the temperature information from the API call
        temperatures = [i["main"]["temp"] for i in data]
        # Filter only dates from API call
        dates = [i["dt_txt"] for i in data]
        # Creating plotly figure to pass into st.plotly_chart() method to create a graph
        # px.line() creates a line chart
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature in F"})
        # Passing the figure object into st.plotly_chart()
        st.plotly_chart(figure)

    # If user selects sky option
    elif option == 'Sky':
        # Filter only the sky conditions from the API call
        condition = [i["weather"][0]["main"] for i in data]
        # Map conditions to paths of images
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        # Filter dates 
        dates = [i["dt_txt"] for i in data]
        # Render images 
        st.image([images[i] for i in condition], caption=dates, width=100)