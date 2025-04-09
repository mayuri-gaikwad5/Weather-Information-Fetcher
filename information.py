import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city_name = city_entry.get().strip()
    
    if not city_name:
        messagebox.showwarning("Input Required", "Please enter a city name.")
        return
    
    API_key = '62bc59743ea0be3e1fd3d2f6658805a1'  # Replace with your OpenWeatherMap API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather = data['weather'][0]['description'].title()
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            weather_info = (
                f"City: {data['name']}\n"
                f"Weather: {weather}\n"
                f"Temperature: {temp} °C\n"
                f"Feels Like: {feels_like} °C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            result_label.config(text=weather_info, fg="black")
        else:
            result_label.config(text="City not found. Please enter a valid city name.", fg="red")

    except requests.exceptions.RequestException:
        result_label.config(text="Network error. Please try again later.", fg="red")

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("400x350")
root.configure(bg="#e0f7fa")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🌤 Weather Checker", font=("Helvetica", 18, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10)

# City Entry
city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 12), bg="#e0f7fa")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
city_entry.pack(pady=5)
city_entry.focus()

# Fetch Button
fetch_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12, "bold"), bg="#00796b", fg="white", command=get_weather)
fetch_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#e0f7fa", justify="left")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
