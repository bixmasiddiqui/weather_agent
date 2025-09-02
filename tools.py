#mocked function
#ham bana rahy hn weather agent
import re


def get_weather(city: str)-> str:
    weather_data = {
        "Karachi": "34°C",
        "Lahore": "36°C",
        "Islamabad": "32°C",
        "London": "20°C",
        "New York": "25°C" 
    }
    return weather_data.get(city, "city not found")

def agent(user_input: str):
    # check if user asked about weather
    match = re.search(r"weather in ([a-zA-Z ]+)", user_input, re.IGNORECASE)
    if match:
        city = match.group(1).strip()
        return get_weather(city)
    else:
        return "Mujhe samajh nahi aaya, please weather ka question poocho."




print(agent("What’s the weather in Karachi?"))
print(agent("What’s the weather in London?"))
print(agent("Hello, how are you?"))
print(agent("add 4 into 8?"))