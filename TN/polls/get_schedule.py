import requests
import json

def connect_schedule(country,op,obpd,dp,ipd):
    link = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/{0}/{1}/{2}/{3}/{4}/{5}".format(country,'PLN','pl-PL',op,dp,obpd)
    url = link

    querystring = {"inboundpartialdate":"2021-12-01"}

    headers = {
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    t = response.json()
    return t
