from datetime import date
import time
import requests
from plyer import notification

# Retrieving data from the web
covid_data = None
url = 'https://corona-rest-api.herokuapp.com/Api/'
try:
    covid_data = requests.get(url)
except:
    print('Oops! Please, check your internet connection.')

# The Loop
if covid_data != None:
    data = covid_data.json()['Success']
    for item in data:
        if item['country'] == 'Argentina':
            data_argentina = item
    while True:
        now = date.today()
        dt = now.strftime('%B %d, %Y')
        totalcases = data_argentina['cases']
        todaycases = data_argentina['todayCases']
        totaldeaths = data_argentina['deaths']
        todaydeaths = data_argentina['todayDeaths']    
        notification.notify(
            title = f'COVID19 stats on Argentina on {dt}',
            message = f'Total cases: {totalcases}\nToday cases: {todaycases}\nTotal deaths: {totaldeaths}\nToday deaths: {todaydeaths}',
            app_icon = 'alert.ico',
            timeout = 15
        )
        time.sleep(60)