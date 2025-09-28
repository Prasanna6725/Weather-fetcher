import requests

API_KEY = "97211b3215facf224ba79e7e89c9bc71"  # Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Something went wrong')}")
            return

        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s\n")

    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
