import requests
import json

def connect_schedule(op,obpd,dp,ipd):
    link = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/{0}/{1}/{2}/{3}/{4}/{5}".format('PL','PLN','pl-PL',op,dp,obpd)
    url = link
    qs = "{}".format(ipd)
    querystring = ''
    if ipd is not None:
        querystring = {"inboundpartialdate":qs}
    else:
        querystring = {"inboundpartialdate": ''}

    headers = {
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    t = response.json()
    return t
