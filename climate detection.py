import requests

def get_current_city():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("city")
    except Exception as e:
        print(f"Location error: {e}")
        return None

def get_weather_no_api(city):
    try:
        url = f"https://wttr.in/{city}?format=3"  # Simple format
        response = requests.get(url)
        print(f"\n📍 Weather for your location:\n{response.text}")
    except Exception as e:
        print(f"Weather error: {e}")

# Main
city = get_current_city()
if city:
    get_weather_no_api(city)
else:
    print("Could not detect your location.")
