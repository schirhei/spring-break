from environment import Env
import pytz
import datetime
import requests

class Castle(Env):

    def __init__(self,city):
        super().__init__(city)
    
    def time_zone_Europe(self):
        if self._city == Canada:
            timezone = 'Europe/Berlin'
            return timezone

    def getCurrentTime(self):
        tz = pytz.timezone(self.timezone)
        ct = datetime.datetime.now(tz=tz)
        # Converting to epoch
        ct = ct.timestamp()
        return self.ct

