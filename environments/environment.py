import requests
import json
import pytz
import datetime


class Env:
    API_KEY = "fa4c879d17d0ff5959bb125a2d7c3c88"
    URL = "api.openweathermap.org/data/2.5/weather?q="

    def __init__(self, city):
        self.city = str(city)
        self._long_url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (self.city, Env.API_KEY)
        self.api = {}
        self.requestAPI()
        print(self.requestAPI())

    def requestAPI(self):
        api = requests.get(self._long_url)
        self.api = api.json()
        return self.api

    def getWeather(self):
        weather = self.api["weather"][0]["main"]
        return weather

    def getSunset(self):
        sunset = self.api["sys"]["sunset"]
        return sunset

    def getSunrise(self):
        sunrise = self.api["sys"]["sunrise"]
        return sunrise

    def getName(self):
        name = self.api["name"]
        return name

    def sos(self):
        return self.sos


    def getCurrentTime(self):
        # tz = pytz.timezone(timezone)
        # ct = datetime.datetime.now(tz=tz)
        # # Converting to epoch
        # ct = ct.timestamp()
        # return self.ct
        return

    def backgroundSwitch(self):
        if self.ct > self.risetime and self.ct < self.settime:
            switch = "bright"
        else:
            switch = "dark"
        return self.switch
