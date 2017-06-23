import requests
from twilio.rest import Client

key = "afc5ee1e717b4776ab74680fafbfc091P"

req = requests.get("https://developer.cumtd.com/api/v2.2/json/GetReroutes" +
                   "?key=" + key)
data = req.json()

for reroute in data['reroutes']:
	hello = "Reroute from " + reroute['start_date'] + " to " + reroute['end_date']

print(hello)

client = Client("AC52ebfb8b6d2f2dd11b83099afdf81701P", "34f4ddc1875e9c61e7b409286ce27b56P")
client.messages.create(to="+14089405637P",from_="+14159692206P",body=hello)
