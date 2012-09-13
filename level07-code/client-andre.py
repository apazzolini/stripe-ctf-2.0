#!/usr/bin/env python
import hashlib
import json
import sys
import urllib

import requests

class ClientError(Exception):
    pass

class Client(object):
    def __init__(self):
        #self.endpoint = "https://level07-2.stripe-ctf.com/user-anacqwycpv/"
        #self.api_secret = "yZgPgM4BXeVNry"
        self.endpoint = "http://localhost:9233/"
        self.api_secret = "nru5L2Qv1DWhCM"
        self.user_id = 5
        self.coords = [128, 30]
        self.waffle_name = "belgian"
        self.count = 1

    def order(self):
        """Order one or more waffles."""
        params = {'waffle': self.waffle_name, 'count': self.count,
                  'lat': self.coords[0], 'long': self.coords[1]}
        return self.api_call('/orders', params)

    def api_call(self, path, params, debug_response=True):
        """Make an API call with parameters to the specified path."""
        body = self._make_post(params)
        resp = requests.post(self.endpoint + path, data=body)

        # for debugging
        if debug_response:
            return resp

        # try to decode response as json
        data = None
        if resp.headers['content-type'] == 'application/json':
            try:
                data = json.loads(resp.text)
            except ValueError:
                pass
            else:
                # raise error message if any
                error = data.get('error')
                if error:
                    raise ClientError(error)

        # raise error on non-200 status codes
        resp.raise_for_status()

        # return response data decoded from JSON or just response body
        return data or resp.text

    def _make_post(self, params):
        params['user_id'] = self.user_id
        body = urllib.urlencode(params)

        sig = self._signature(body)
        body += '|sig:' + sig
        
        
        requests.post('https://level07-2.stripe-ctf.com/user-anacqwycpv/orders', data='count=10&lat=37.351&user_id=1&long=-119.827&waffle=eggo\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02(&waffle=liege|sig:4ab2fe31cc960b3c2b26c70af2637bacab49b474')
        
        
        return 
        
        return body

    def _signature(self, message):
        h = hashlib.sha1()
        h.update(self.api_secret + message)
        return h.hexdigest()

if __name__ == '__main__':
    c = Client()
    print c.order()
