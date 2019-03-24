#This code sample uses requests (HTTP library)
import requests
import json

payload = {'grant_type': 'password',
           'username': "jonducrou@gmail.com",
           'password': open('netatmo-password','r').read().rstrip(),
           'client_id':"5c96e6fff1c1e02e618c61a5",
           'client_secret': open('netatmo-client-secret','r').read().rstrip(),
           'scope': 'read_station'}
try:
    response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    response.raise_for_status()
    access_token=response.json()["access_token"]
    refresh_token=response.json()["refresh_token"]
    scope=response.json()["scope"]
#    print("Your access token is:", access_token)
#    print("Your refresh token is:", refresh_token)
#    print("Your scopes are:", scope)

    params = {
        'access_token': access_token,
        'device_id': '70:ee:50:28:ea:08'
    }

    response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
    response.raise_for_status()
    data = response.json()["body"]
    #print(json.dumps(data, indent=4, sort_keys=True))
    for mod in data["devices"][0]["modules"]:
        #print(json.dumps(mod, indent=4, sort_keys=True))
        if "sum_rain_24" in mod["dashboard_data"]:
            print("Rain: " + str(mod["dashboard_data"]["sum_rain_24"]))
        if "Humidity" in mod["dashboard_data"]:
            print("Humidity: " + str(mod["dashboard_data"]["Humidity"]))
        if "Temperature" in mod["dashboard_data"]:
            print("Temperature: " + str(mod["dashboard_data"]["Temperature"]))
        if "WindStrength" in mod["dashboard_data"]:
            print("WindStrength: " + str(mod["dashboard_data"]["WindStrength"]))

except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)
