import tkinter as tk
import requests # Download this library using pip install request!!!!!!!
from tkinter import font
from PIL import Image, ImageTk # Download this library using pip install Pillow!!!!!1

HEIGHT = 500
WIDTH = 600

def format(c_weather):





    try:

        name = c_weather['name']
        city_id = c_weather['id']
        desc = c_weather['weather'][0]['description']
        temp = c_weather['main']['temp']
        humd = c_weather['main']['humidity']
        visb = c_weather['visibility']
        wins = c_weather['wind']['speed']
		icona = c_weather['weather'][0]['icon']
        final_print =  'City name: %s \nConditions: %s \nTemperature (°C): %s \nHumidity (percent) : %s \nVisibility (m):%s \nWind speed(Km/h)  : %s ' % (name, desc, temp,humd,visb,wins,icona)
    except :
        final_print = 'Problem Occured'
    return final_print

def weather(city):
    wea_key = 'b1d5f70b111bc79129ae64927af193de'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    par = {'APPID': wea_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params= par)
    c_weather = response.json()
    print(c_weather)

    label['text'] = format(c_weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


# Please start commenting from here!!!!!!


pic = Image.open('/Users/rushanktalwar/Desktop/Weather Background.png')
pic = ImageTk.PhotoImage(pic)
pic_label = tk.Label(image = pic)
pic_label.image = pic
pic_label.place(relheight = 1, relwidth = 1)

# Stop commenting here !!!!!!!


frame =tk.Frame(root, bg="black", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font = ('Bookman Old Style', 23))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font = ('Bookman Old Style', 17), command= lambda: weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='black', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font = ('Bookman Old Style', 23), justify = 'left')
label.place(relwidth=1, relheight=1)




root.mainloop()
