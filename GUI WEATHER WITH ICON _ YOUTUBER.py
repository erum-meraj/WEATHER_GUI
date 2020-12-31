import tkinter as tk
import requests
from tkinter import font
#from PIL import Image, ImageTk

app = tk.Tk()

HEIGHT = 500
WIDTH = 600
'''
def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img
'''
def format_response(c_weather):

    try:

        name = c_weather['name']
        desc = c_weather['weather'][0]['description']
        temp = c_weather['main']['temp']
        humd = c_weather['main']['humidity']
        visb = c_weather['visibility']
        final_str =  'City name: %s \nConditions: %s \nTemperature (°C): %s \nHumidity (percent): %s \nVisibility (m): %s' % (name, desc, temp, humd, visb)
    except :
        final_str = 'Problem Occured'
    return final_str


def weather(city):
    wea_key = 'b1d5f70b111bc79129ae64927af193de'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    par = {'APPID': wea_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params= par)
    c_weather = response.json()
    results['text'] = format_response(c_weather)
'''
    icon_name = c_weather['weather'][0]['icon']
    open_image(icon_name)
'''

C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
'''
background_image= tk.PhotoImage(file='/Users/rushanktalwar/Desktop/Weather Background.png')
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
'''
C.pack()


frame =tk.Frame(app, bg="black", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font = ('Bookman Old Style', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font = ('Bookman Old Style', 14), command= lambda: weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='black', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, justify = 'left')
label.place(relwidth=1, relheight=1)

results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=('Bookman Old Style', 15), bg='#ffffff')
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg='#ffffff', bd=0, highlightthickness=0)
weather_icon.place(relx=.6, rely=0, relwidth=1, relheight=0.5)

app.mainloop()