import requests
import time
from dateutil import parser

toople_list = []
key = "afc5ee1e717b4776ab74680fafbfc091"

req = requests.get("https://developer.cumtd.com/api/v2.2/json/GetReroutes" +
                   "?key=" + key)
data = req.json()
current_date = time.strftime("%x")

for reroute in data['reroutes']:
    for bus in reroute['affected_routes']:
        if parser.parse(reroute['start_date']) <= parser.parse(current_date) <= parser.parse(reroute['end_date']):
            combined_name = bus['route_short_name'] + " " + bus['route_id']
            color = bus['route_color']
            toople = (combined_name, color)
            toople_list.append(toople)

toople_list = list(set(toople_list))
print(toople_list)
