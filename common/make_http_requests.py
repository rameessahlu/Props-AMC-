from . import config as c
import requests, json

def make_post_request(address):
    contents =  requests.post(c.URL.format(address,c.API_KEY))
    return json.loads(contents.text)
