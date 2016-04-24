#!/usr/bin/env python
import os
import json
import requests
from collections import defaultdict

KEY = os.getenv('UNTAPPD_KEY')
KEY_SECRET = os.getenv('UNTAPPD_SECRET')

class untappd(object):
    URL = 'https://api.untappd.com/v4'

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret


    def get(self, type, info, id, results=50, offset=0):
        d = requests.get('{}/{}/{}/{}/?limit={}&offset={}&client_id={}'
                         '&client_secret={}'.format(self.URL, type, info, id,
                                                    results, offset, self.key,
                                                    self.secret))
        return json.loads(d.content)


    def search(self, type, id, results=50, offset=0):
        d = requests.get('{}/search/{}/?q={}&limit={}&offset={}&client_id={}'
                         '&client_secret={}'.format(self.URL, type, id,
                                                    results, offset, self.key,
                                                    self.secret))
        return json.loads(d.content)


    def gather_data(self, start, nbr, request_info=['user', 'beers', None]):
        try:
            beers = defaultdict(list)
            for i in range(start, start + nbr, 50):
                print 'Getting records {} through {}...'.format(i + 1, i + 50)
                d = get(self, request_info[0], request_info[1],
                        request_info[2], offset=start)
                beers['bid'].append([x.get('bid') for x in d['response']['beers']['items']['beer']])
                beers['beer_name'].append([x.get('beer_slug') for x in d['response']['beers']['items']['beer']])
                beers['total_ratings'].append([x.get('rating_count') for x in d['response']['beers']['items']['beer']])
                beers['overall_rating'].append([x.get('rating_score') for x in d['response']['beers']['items']['beer']])
                beers['user_rating'].append([x.get('rating_score') for x in d['response']['beers']['items']])

            return beers
        except:
            pass
