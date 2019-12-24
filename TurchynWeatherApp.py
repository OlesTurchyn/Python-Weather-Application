#Name: Oles Turchyn
#Date: December 14, 2019
#Project: Weather Application 

import tkinter as tk
from tkinter import*
from tkinter import ttk 
import requests

win = tk.Tk()
tk.Tk.wm_title(win, "Turchyn Weather App")

#Set height and width variables for main canvas 
HEIGHT = 600
WIDTH = 400

#Weather API (7435744763a6eef7e5787f336bf76e65)
#api.openweathermap.org/data/2.5/weather?q={city name}

#Call for OpenWeather API using the key and URL
def format_response(weather):
    try:
        name = weather['name']
        country = weather ['sys']['country']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str= 'City: %s \nCountry: %s \nConditions: %s \nTemperature (°C): %s' % (name, country, desc, temp)
    except:
        final_str = 'Error'

    return final_str

# Call for openweather API using the API Key and URL
def get_weather(city):
    weather_key = '7435744763a6eef7e5787f336bf76e65'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather =response.json()

    label['text'] = format_response(weather)

#Set Primary Canvas
canvas = tk.Canvas(win, height = HEIGHT, width = WIDTH,)
canvas.pack()

background_image = tk.PhotoImage(file='')

background_label = tk.Label(win, image=background_image)
background_label.place(relwidth=1,relheight=1)

#Title frame setup 
title = tk.Frame(win, bd = 5)
title.place(relx=0.5, rely =0.0001, relwidth = 0.75, relheight = 0.1, anchor='n')

title_label = tk.Label(title, text = "Turchyn Weather App", font=('Times New Roman', 15))
title_label.place(relwidth = 1, relheight = 1)

#User frame setup 
frame = tk.Frame(win, bg='#025cbd',bd=5)
frame.place(relx=0.5, rely=0.1, relwidth = 0.75, relheight = 0.1, anchor='n')

#User input entry box setup
entry = ttk.Entry(frame, font = 65)
entry.place(relwidth=0.65, relheight=1)

#Get weather button setup 
button = ttk.Button(frame,text="Get Weather",command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

#Result frame setup 
lower_frame = tk.Frame(win, bg='#025cbd', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor = 'n')

label = tk.Label(lower_frame, font=('Times New Roman', 15), anchor = 'nw', justify = 'left', bd = 4)
label.place(relwidth=1,relheight=1)

#Close frame setup 

close_frame = tk.Frame(win, bd = 10)
close_frame.place(relx = 0.5, rely = 0.96, relwidth=0.75, relheight= 0.1, anchor = 's')

#Close button setup 
close_button = ttk.Button(close_frame, text ="Exit", command = win.quit)
close_button.place(relwidth=1, relheight=1)

win.mainloop()
