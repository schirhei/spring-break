from environment import Env
from env_castle import Castle
import requests
import urllib.request
import httplib2
import pygame
import json
import pytz
import datetime
import pygame

def main():
    print("jaja")
    #taking user input
    location = input("Location")
    if location == "Castle":
        castle = Castle('Schwangau', 'DE','Europe/Berlin')
        name = castle.getName()
        switch = castle.backgroundSwitch()
    elif location == "Vancouver":
        castle = Castle('Vancouver', 'CA', 'Canada/Pacific')
        name = castle.getName()
        switch = castle.backgroundSwitch()
    elif location == "Japan":
        castle = Castle('Tokyo', 'JP', 'Japan')
        name = castle.getName()
        switch = castle.backgroundSwitch()
    elif location == "Pole":
        castle = Castle('North Pole', 'US', 'US/Alaska')
        name = castle.getName()
        switch = castle.backgroundSwitch()
    elif location == "Desert":
        castle = Castle('Niamey', 'NE', 'Africa/Niamey')
        name = castle.getName()
        switch = castle.backgroundSwitch()
    else:
        print("Location selected is invalid")
        switch = "None"

    #insert the background here
    if switch == "Dark":
        print("FAFA")
    elif switch == "Bright":
        print("EWEW")
    else:
        print("Location weather cannot be determined")

    #long_url = "http://%s%s,%s&appid=%s" % (Castle.URL, Castle.CITY, Castle.COUNTRY, Castle.API_KEY)
    #print(long_url)
    #get_req = request.GET(long_url)
    #print(get_req.coord.long)
    #get_req = urllib.request.urlopen(long_url).read()
    #print(get_req.coord.long)
    #resp, content = httplib2.Http().request(long_url)
    #print(resp)
    #api = requests.get(long_url)
    #api =api.json()
    #settime = api["sys"]["sunset"]
    #risetime = api["sys"]["sunrise"]
    #print(api["sys"]["sunset"])
    #print(api["sys"]["sunrise"])
    #tz = pytz.timezone('Japan')
    #ct = datetime.datetime.now(tz=tz)
    #print(ct)
    #Converting to epoch
    #ct = ct.timestamp()
    #print(ct)
    #if (ct >  risetime and ct < settime):
    #    print("bright")
    #else:
    #    print ("dark")

if __name__ == '__main__':
    main()
