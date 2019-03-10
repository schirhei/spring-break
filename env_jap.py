from environment import Env
import pytz
import datetime
import requests

class Jap(Env):

    def __init__(self):
        super().__init__(self.long_url)

    city = "Tokyo"
    country = "JP"
    long_url = "http://%s%s,%s&appid=%s" % (Env.URL, city,country, Env.API_KEY)
    timezone = 'Japan'

    def requestAPI(self):
        long_url = requests.get(self.api)
        long_url = self.URL + self.city + self.country + self.API_KEY
        self.api = self.api.json()