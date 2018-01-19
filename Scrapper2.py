import requests
import json
import csv
import urllib2
#need to modify the API
api_token = "RhaEiTQBNGNWZxnEfJhDpU3HmLbFTpz6Sw0HxAX9GCqtCrz1KqPEyfpgKiMrAOIY"
api_url_base = "https://www.thebluealliance.com/api/v3/"

headers = {"contentType": "application/json",
           "authorization": api_url
           }
def get_content ():
    api_url ='{0}content'.format(api_url_base)
    response = requests.get(api_url, headers = headers)


