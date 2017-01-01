#!/usr/bin/python
import json
import os
import requests


class Untappd(object):
    API_EP = 'https://api.untappd.com/v4'

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def _add_keys(self, kwargs):
        kwargs['client_id'] = self.key
        kwargs['client_secret'] = self.secret

        return kwargs

    def info(self, entity, action, identity, **kwargs):
        kwargs = self._add_keys(kwargs)

        path = os.path.join(self.API_EP, entity, action, identity)
        d = requests.get(path, params=kwargs)

        return json.loads(d.content)

    def search(self, entity, q, **kwargs):
        kwargs = self._add_keys(kwargs)
        kwargs['q'] = q

        path = os.path.join(self.API_EP, 'search', entity)
        d = requests.get(path, params=kwargs)

        return json.loads(d.content)

    def feed(self, entity, action, **kwargs):
        kwargs = self._add_keys(kwargs)

        path = os.path.join(self.API_EP, entity, action)
        d = requests.get(path, params=kwargs)

        return json.load(d.content)

    def specific_feed(self, entity, action, identity, **kwargs):
        kwargs = self._add_keys(kwargs)

        path = os.path.join(self.API_EP, entity, action, identity)
        d = requests.get(path, params=kwargs)

        return json.load(d.content)
