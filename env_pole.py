from environment import Env
import pytz
import datetime
import requests

class Pole(Env):

    def __init__(self, city, country, timezone):
        super().__init__(city, country, timezone)

    city= "North Pole"
    country = "US"
    long_url = "http://%s%s,%s&appid=%s" % (Env.URL, city,country, Env.API_KEY)
    timezone = 'US/Alaska'

    def requestAPI(self):
        long_url = requests.get(self.api)
        long_url = self.URL + self.city + self.country + self.API_KEY
        self.api = self.api.json()