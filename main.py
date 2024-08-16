# Import statements
import streamlit as st
import plotly.express as px

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

# Creating a function to dynamically plot fake data
def get_data(days):
    # Creating a dummy date list to store dates 
    dates = ["2022-10-25","2022-10-26","2022-10-27"]  
    # Creating a dummy temperatures list to store temperatures 
    temperatures = [23, 31, 36]
    # Adjusting temperatures to be dynamic
    temperatures = [days * i for i in temperatures]
    # Return dates and temperatures
    return dates, temperatures
# Calling get_data to dynamically get data points for line graph and deconstructing
# the returned tuple into variables d and t
d,t = get_data(days)

# Creating plotly figure to pass into st.plotly_chart() method to create a graph
# px.line() creates a line chart
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature in F"})

# Passing the figure object into st.plotly_chart()
st.plotly_chart(figure)