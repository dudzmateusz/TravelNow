import requests

def photos(id_hotel):
    url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

    querystring = {"id":id_hotel}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    t = response.json()
    return t