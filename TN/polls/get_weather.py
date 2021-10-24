import requests
import datetime

def weather(city):
    url = "https://visual-crossing-weather.p.rapidapi.com/forecast"
    b = []
    querystring = {"location":city,"aggregateHours":"24","shortColumnNames":"0","unitGroup":"metric","contentType":"json"}

    headers = {
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5",
        'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    t = response.json()
    try:
        for i in t['locations'][city]['values']:
            i['datetimeStr']= datetime.datetime.strptime(i['datetimeStr'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d/%m/%y')
            b.append(i)
    except:
        b.append('empty')
    return b
