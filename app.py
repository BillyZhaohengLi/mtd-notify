import requests, time
from dateutil import parser
from flask import Flask, render_template
from pprint import pprint

app = Flask(__name__)

def reroute_info():
    toople_list = []
    key = "afc5ee1e717b4776ab74680fafbfc091"

    req = requests.get("https://developer.cumtd.com/api/v2.2/json/GetReroutes" +
                       "?key=" + key)
    data = req.json()
    current_date = time.strftime("%x")

    mapping = {
        1: '1 Yellow',
        100: '100 Yellow',
        2: '2 Red',
        20: '20 Red',
        3: '3 Lavender',
        30: '30 Lavender',
        4: '4 Blue',
        5: '5 Green',
        50: '50 Green',
        6: '6 Orange',
        7: '7 Grey',
        70: '70 Grey',
        8: '8 Bronze',
        9: '9 Brown',
        10: '10 Gold',
        11: '11 Ruby',
        110: '110 Ruby',
        12: '12 Teal',
        120: '120 Teal',
        13: '13 Silver',
        130: '130 Silver',
        14: '14 Navy',
        16: '16 Pink',
        18: '18 Lime',
        180: '180 Lime',
        21: '21 Raven',
        22: '22 Illini',
        220: '220 Illini',
        280: '280 tranSPORT',
    }

    for reroute in data['reroutes']:
        for bus in reroute['affected_routes']:
            if parser.parse(reroute['start_date']) <= parser.parse(current_date) <= parser.parse(reroute['end_date']):
                combined_name = mapping.get(int(bus['route_short_name']), None)
                bus_color = bus['route_color']
                message = reroute['message']
                toople = (combined_name, message, bus_color)
                toople_list.append(toople)

    toople_list = list(set(toople_list))
    toople_list = sorted(toople_list, key=lambda x: int(x[0].split(' ')[0]))

    reasons = dict()
    for item in toople_list:
        key = item[0] + "," + item[2]
        val = item[1]
        if(key in reasons):
            reasons[key].add(val)
        else:
            reasons[key] = {val}

    # pprint(reasons, width=200)
    return reasons

@app.route('/')
def hello():
    data = reroute_info()
    del data['9 Brown,825622']
    print(data)
    return render_template('index.html', data=data)

app.run(host='0.0.0.0', port=5000)

# print(toople_list)
