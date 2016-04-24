#!/usr/bin/env python
import os
import json
import requests

from classes import *

# start crawl of data
auth = untappd(KEY, KEY_SECRET)

# from user, grab total number of beers checked-in
user = auth.get('user', 'info', 'hooverm2')
tot_beers = user['response']['user']['stats']['total_beers']

# use total number of beers to set up loop to grab all data
# beers = auth.get('user', 'beers', 'hooverm2')

