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


if __name__ == '__main__':
    main()
