# Import statements
import streamlit as st

# Creating title for the web app
st.title("Weather Forecast For The Next Days")
# Creating text input widget and storing its value in place variable
place = st.text_input(label="Place:")
# Creating slider to determine # of days and storing its value in days variable
days = st.slider(label="Forecast Days", min_value=1, max_value=5, 
                help= "Select the number of forecasted days")
# Creating drop down option menu and storing its value in option variable
option = st.selectbox(label="Select data to view", options=("Temperature", 
                     "Sky"))
# Creating subheader for graph
st.subheader(f"{option} for the next {days} days in {place}")
print(place)
print(days)