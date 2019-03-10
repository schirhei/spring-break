from environment import Env
import pytz
import datetime
import requests

class Des(Env):

    def __init__(self):
        super().__init__(self.long_url)

    city= "Niamey"
    country = "NE"
    long_url = "http://%s%s,%s&appid=%s" % (Env.URL, city,country, Env.API_KEY)
    timezone = 'Africa/Niamey'

    def requestAPI(self):
        long_url = requests.get(self.api)
        long_url = self.URL + self.city + self.country + self.API_KEY
        self.api = self.api.json()