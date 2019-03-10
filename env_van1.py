from environment import Env
import pytz
import datetime
import requests

class Van(Env):

    def __init__(self, city, country, timezone):
        super().__init__(city, country, timezone)

    city= "Vancouver"
    country = "CA"
    long_url = "http://%s%s,%s&appid=%s" % (Env.URL, city,country, Env.API_KEY)
    timezone = "Canada/Pacific"

    def time_zone(self):
        return self.timezone

