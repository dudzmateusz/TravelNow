import json
import requests

def send(message,telephone):
    url = "https://d7sms.p.rapidapi.com/secure/send"

    payload = {
        'content': str(message),
        'from': 'TNMD',
        'to': telephone }
    dataq = json.dumps(payload)
    headers = {
        'content-type': "application/json",
        'authorization': "Basic YmJ2cTQwNzc6VWQwNmpOeWo=",
        'x-rapidapi-key': "02e56c89e5mshc3f1b1fd23b0a8dp152556jsnd2f5cf93b8b5",
        'x-rapidapi-host': "d7sms.p.rapidapi.com"
        }
    response = requests.request("POST", url, data=dataq, headers=headers)
    rc = response.content
    print(rc)
    return response