# Import statements
import requests

API_KEY = "8de3beaa830a23253f5181daf1bada14"
API_KEY2 = "141710af2113bab9f55ef73e1bcd33d5"

# Creating function to get data
def get_data(city, country, days, option):
    # Construct query URL to send to OpenWeather API
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={API_KEY2}"
    # Send our request to the OpenWeather API and store response into response variable
    response = requests.get(url)
    # Format response variable into a JSON
    contents = response.json()
    # Storing number of data points that our API response should have (remember this API 
    # gives us data per every 3 hours... Since 3 goes into 24 8 times, we multiply days
    # by 8 to give us the correct amount of data points)
    data_points = days * 8
    # Filtering the response based on data that we want which is stored in the "list" key of the JSON
    filtered_list = contents["list"]
    # Filtering our filtered list to only have data equating to number of days passed in
    filtered_list = filtered_list[:data_points]
    # Filtering data based on options 
    match option:
        # If the option is temperature
        case "Temperature":
           # Filter the list even more to retrieve only temperatures through list comprehension
           filtered_list = [i["main"]["temp"] for i in filtered_list]
           # Return filtered_list 
           return filtered_list
        case "Sky":
            # Filter the list even more to retrieve only conditions through list comprehension
            filtered_list = [i["weather"][0]["main"] for i in filtered_list]
            # Return filtered list
            return filtered_list
print(get_data("Centreville", "USA", 2, "Sky"))
