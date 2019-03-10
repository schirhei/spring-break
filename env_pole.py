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

    def time_zone(self):
        return self.timezone

