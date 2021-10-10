import requests
import json

def place(city):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/PL/PLN/pl-PL/"

    qs = {"query":"{}".format(city)}
    querystring = qs

    headers = {
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    t = response.json()

    return t

def test(list):
    url = "https://airport-info.p.rapidapi.com/airport"
    a = []
    for i in list:

        querystring = {"iata": i}

        headers = {
            'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5",
            'x-rapidapi-host': "airport-info.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        t = response.json()
        a.append(t)
    return a

