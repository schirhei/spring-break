from environment import Env
from env_castle import Castle
import requests
import json
import pytz
import datetime

def main():
    print("jaja")
    vancouver = Castle('Vancouver')
    print(vancouver.getWeather())
    print(vancouver.getSunset())
    print(vancouver.getSunrise())

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
