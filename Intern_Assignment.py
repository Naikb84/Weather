import requests

def get_weather_data():
    date = input("Enter the date (YYYY-MM-DD format): ")
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London.us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    data = response.json()
    for entry in data['list']:
        if entry['dt_txt'].split(' ')[0] == date:
            return entry['main']['temp']

def get_wind_speed_data():
    date = input("Enter the date (YYYY-MM-DD format): ")
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London.us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    data = response.json()
    for entry in data['list']:
        if entry['dt_txt'].split(' ')[0] == date:
            return entry['wind']['speed']

def get_pressure_data():
    date = input("Enter the date (YYYY-MM-DD format): ")
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London.us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    data = response.json()
    for entry in data['list']:
        if entry['dt_txt'].split(' ')[0] == date:
            return entry['main']['pressure']

def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"The temperature on the chosen date is {get_weather_data()}°C.")
        elif choice == 2:
            print(f"The wind speed on the chosen date is {get_wind_speed_data()} m/s.")
        elif choice == 3:
            print(f"The pressure on the chosen date is {get_pressure_data()} hPa.")
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
