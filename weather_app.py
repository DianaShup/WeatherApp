import tkinter as tk
from tkinter import *
import datetime

import requests
from PIL import Image, ImageTk

# 2e92601da79196587ca793c5b5fe3b39
# 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

current = tk.Tk()
current.geometry("700x370")
current.title("Current weather")

def add_item():

    actions_box.insert(0, textbox.get())
    textbox.delete(0, END)




def create_window():
    infoo = Toplevel(current)
    infoo.geometry("600x370")
    infoo.title("About application")
    background_image1 = PhotoImage(file="winter hsk 2011 16.png")
    background_label1 = Label(infoo, image=background_image1)
    background_label1.place(relwidth=1, relheight=1)
    information = Label(infoo, text = 'This is weather application there you can check current weather description.', bg = 'white', font=('lucida console', 8))
    information.pack()
    information.place(rely = 0.1)
    information2 = Label(infoo, text='You can check current weather in your city. \nEnter your city name in the search bar or enter zip code of this city.',
                        bg='white', font=('lucida console', 8))
    information2.pack()
    information2.place(rely=0.3)
    information3 = Label(infoo,
                         text='A ZIP Code is a postal code used by the United States Postal Service.',
                         bg='white', font=('lucida console', 8))
    information3.pack()
    information3.place(rely=0.5)
    frame1 = Frame(infoo, image = background_image1, bd=5)
    frame1.place(relwidth=1, relheight=1)







my_menu = Menu(current)
info = Menu(my_menu, tearoff=0)
info.add_command(label="Info", command=create_window)
info.add_command(label="Exit", command=current.quit)
my_menu.add_cascade(label='About aplication', menu=info)
current.config(menu=my_menu)



def change_format(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        feels_like = weather['main']['feels_like']
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        wind_direction = weather['wind']['deg']
        now = datetime.datetime.now()
        result = 'Day: %s \nCity: %s \nConditions: %s \nTemperature (°C): %s \nFeels like: %s \nAtmospheric pressure hPa: %s \nHumidity: %s \nWind speed meter/sec: %s \nWind direction (degrees): %s' % (now.strftime("%d-%m-%Y %H:%M"),
            name, desc, temp, feels_like, pressure, humidity, wind_speed, wind_direction)
    except:

        if textbox.get()[0] == 'L':
            result = "Maybe you are searching for: \nLondon\nLublin\nLincoln\nLiverpool\nLviv"
        elif textbox.get()[0] == 'A':
            result = 'Maybe you are searching for: \nAbu Dhabi\nAlexandria\nAmsterdam\nAnkara\nAthens'
        elif textbox.get()[0] == 'B':
            result = 'Maybe you are searching for: \nBaku\nBangkok\nBarcelona\nBelfast\nBergen'
        elif textbox.get()[0] == 'C':
            result = 'Maybe you are searching for: \nCardiff\nCasablanca\nChelyabinsk\nChicago\nCambridge'
        elif textbox.get()[0] == 'D':
            result = 'Maybe you are searching for: \nDallas\nDenver\nDnipro\nDubai\nDublin'
        elif textbox.get()[0] == 'E':
            result = 'Maybe you are searching for: \nEdinburgh\nErfurt'
        elif textbox.get()[0] == 'F':
            result = 'Maybe you are searching for: \nFlorence\nFuji'
        elif textbox.get()[0] == 'G':
            result = 'Maybe you are searching for: \nGeneva\nGdańsk'
        elif textbox.get()[0] == 'H':
            result = 'Maybe you are searching for: \nHelsinki\nHonolulu'
        elif textbox.get()[0] == 'I':
            result = 'Maybe you are searching for: \nIzumo'
        elif textbox.get()[0] == 'K':
            result = 'Maybe you are searching for: \nKansas City\nKabul'
        elif textbox.get()[0] == 'M':
            result = 'Maybe you are searching for: \nMadrid\nMexico'
        elif textbox.get()[0] == 'O':
            result = 'Maybe you are searching for: \nOpole\nOrsk\nOslo'
        elif textbox.get()[0] == 'P':
            result = 'Maybe you are searching for: \nParis\nPinsk\nPodolsk'
        elif textbox.get()[0] == 'R':
            result = 'Maybe you are searching for: \nReykjavik\nRiga\nRome\nRotterdam\nRzeszów'
        elif textbox.get()[0] == 'S':
            result = 'Maybe you are searching for: \nSaint Petersburg\nSan Francisco\nSantiago\nSeoul\nShanghai'
        elif textbox.get()[0] == 'T':
            result = 'Maybe you are searching for: \nTallinn\nTambov\nTbilisi'
        elif textbox.get()[0] == 'U':
            result = 'Maybe you are searching for: \nUlan-Ude'
        elif textbox.get()[0] == 'V':
            result = 'Maybe you are searching for: \nValencia\nVictoria\nVienna\nVilnius\nVitebsk'
        elif textbox.get()[0] == 'W':
            result = 'Maybe you are searching for: \nWarsaw\nWrocław\nWellington\nWindsor'
        elif textbox.get()[0] == 'Y':
            result = 'Maybe you are searching for: \nYork\nYakutsk'
        elif textbox.get()[0] == 'Z':
            result = 'Maybe you are searching for: \nZagreb'

        else:
            result = 'Invalid info'
    return result


def get_weather(city):
    key = '2e92601da79196587ca793c5b5fe3b39'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parametrs = {'APPID': key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=parametrs)
    print(response.json())
    weather = response.json()

    results['text'] = change_format(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)
    add_item()


def open_image(icon):
    size = int(lower_frame.winfo_height() * 0.45)
    img = ImageTk.PhotoImage(Image.open('./icon/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


background_image = tk.PhotoImage(file="winter hsk 2011 16.png")
background_label = tk.Label(current, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(current, bg='#A9E2F3', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.1, anchor='n')


entry_text = StringVar()
textbox = tk.Entry(frame, font=40, textvariable=entry_text)
textbox.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Search', font=40, command=lambda: get_weather(textbox.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


lower_frame = tk.Frame(current, bg='#A9E2F3', bd=10)
lower_frame.place(relx=0.4, rely=0.25, relwidth=0.5, relheight=0.6)

frame_city = tk.Frame(current, bg='#A9E2F3', bd=10)
frame_city.place(relx=0.2, rely=0.35, relwidth=0.3, relheight=0.5, anchor='n')

list_of_cities = Label(current, text='Last wanted cities',
                    bg='#A9E2F3', font=('lucida console', 8))
list_of_cities.pack()
list_of_cities.place(relx =0.1,rely=0.3)



def use_selected_action():

    query = actions_box.get(actions_box.curselection()[0])
    entry_text.set(query)


actions_box = Listbox(frame_city, bd = 4)
actions_box.config(bg = 'white')
actions_box.place(relwidth=1, relheight=1)

cities = []
for city in cities:
     add_item()




scrollbar = Scrollbar(actions_box)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=actions_box.yview)

useBtn = Button(frame_city, text='Put', command=use_selected_action)
useBtn.place(relx = 0.45, rely = 0.8)

label = tk.Label(lower_frame, font=('lucida console', 15))
label.place(relwidth=1, relheight=1)

results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg='white')
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

current.mainloop()
