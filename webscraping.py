import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09927000000005&lon=-118.33806999999996#.XIRJS1NKgUE')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

'''
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
'''
period_name = [item.find(class_='period-name').get_text() for item in items]
short_descriptions= [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather_stuff = pd.DataFrame(
    {
        'period':period_name,
        'short_descriptions': short_descriptions,
        'temperatures': temperatures,
    }
)
print(weather_stuff)
weather_stuff.to_csv('weather.csv', index=None)