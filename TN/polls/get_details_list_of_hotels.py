import requests

def details_hotels(destinationId,checkIn,checkOut,adults):
    url = "https://hotels4.p.rapidapi.com/properties/list"
    querystring = {"destinationId":destinationId,"pageNumber":"1","pageSize":"25","checkIn":checkIn,"checkOut":checkOut,"adults1":adults,"sortOrder":"PRICE","locale":"pl_PL","currency":"PLN"}

    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    t = response.json()
    print(t)
    return t
