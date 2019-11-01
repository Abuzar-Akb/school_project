import http.client
import urllib.parse
import datetime
import json
from tkinter.messagebox import showinfo
from tkinter import *
from time import *


def stations():  # new window definition

    key = {'Ocp-Apim-Subscription-Key': 'a97597eb7db7471b94e741b544e39062'}

    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request(
        "GET", "/public-reisinformatie/api/v2/stations", headers=key)
    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    payloadObject = data['payload']
    station_dict = {}
    for station in payloadObject:
        station_dict.update({station["code"]: station["namen"]["lang"]})

    print(station_dict)


stations()
