#!/usr/bin/env python
import os
import json
import requests

KEY = os.getenv('UNTAPPD_KEY')
KEY_SECRET = os.getenv('UNTAPPD_SECRET')

class untappd(object):
    URL = 'https://api.untappd.com/v4'

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret


    def get(self, type, info, id):
        d = requests.get('{}/{}/{}/{}/?client_id={}&client_secret={}'
                         .format(URL, type, info, id, self.key, self.secret))
        return json.loads(d.content)


    def search(self, type, id):
        d = requests.get('{}/search/{}/?q={}&client_id={}&client_secret={}'
                         .format(URL, type, id, self.key, self.secret))
        return json.loads(d.content)
