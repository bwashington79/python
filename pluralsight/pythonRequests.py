import requests
import json

response = requests.get("http://api.open-notify.org/astros")
print(response.status_code)
print(type(response.encoding))
# print(response.content)
responseJson = json.loads(response.content.decode('utf-8'))
print(type(responseJson))
print(responseJson['people'][1]['name'])
# parsJson = json(response[0])

