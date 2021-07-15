import requests

def get_countries():
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/pl-PL"

    headers = {
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5",
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    t = response.json()
    a = ()
    b = list(a)
    for i in t['Countries']:
        b.append((i['Code'],i['Name']),)
    a = tuple(b)
    return a

