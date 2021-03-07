import os
import urllib.request

day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13d.png', '50d.png']
night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

base_url = 'https://openweathermap.org/img/w/'
icon_direction = './icon/'
if not os.path.exists(icon_direction):
	os.makedirs(icon_direction)

# Get the day weather icons
for name in day:
	file_name = icon_direction + name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)

# Repeat the same thing for night weather icons
for name in night:
	file_name = icon_direction + name
	if not os.path.exists(file_name):
		urllib.request.urlretrieve(base_url+name, file_name)

