import requests


def location(city):
    destID = str()

    url = "https://hotels4.p.rapidapi.com/locations/search"
    qs = {"query": "{}".format(city)}
    querystring = qs
    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    t = response.json()
    for i in t['suggestions']:
        for ix in i['entities']:
            if ix:
                destID = str(ix['destinationId'])
    print(destID)
    return destID
