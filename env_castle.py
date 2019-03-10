from environment import Env
import pytz
import datetime
import requests

class Castle(Env):

    def __init__(self, city, country,timezone):
        super().__init__(city, country, timezone)

    city = "Schwangau"
    country = "DE"
    long_url = "http://%s%s,%s&appid=%s" % (Env.URL, city,country, Env.API_KEY)
    timezone = 'Europe/Berlin'

    def time_zone_Europe(self):
        timezone = 'Europe/Berlin'
        return timezone


