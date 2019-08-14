from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
import pprint as pp
from builtins import map
from builtins import object
import json, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, ssl, sys, io, gzip
from numbers import Number



class MockConnection(object):
    """
    Object for connection to EMS API
    """

    def __init__(self, user=None, pwd=None, proxies=None, verbose=False, ignore_ssl_errors=False, server="prod",
                 server_url=None):

        self.__user = user
        self.__pwd = pwd
        self.__proxies = proxies
        self.__ntrials = 0
        self.__uri_root = None
        self.__ignore_ssl_errors = ignore_ssl_errors
        self.token = None
        self.token_type = None

    def request(self,
                rtype="GET", uri=None, uri_keys=None, uri_args=None,
                headers=None, body=None, data=None, jsondata=None, proxies=None,
                verbose=False
                ):
        resp_h, content = [], []
        if uri_keys == ('profile', 'search'):
            resp_h = [('Cache-Control', 'no-store, must-revalidate, no-cache'), ('Pragma', 'no-cache'), ('Content-Type', 'application/json; charset=utf-8'), ('Content-Encoding', 'gzip'), ('Vary', 'Accept-Encoding'), ('Server', 'Microsoft-IIS/8.5'), ('X-Adi-Unique-Id', 'a2f0a219-f89a-467c-a087-d0acb8a0ef41'), ('X-Powered-By', 'ARR/3.0'), ('Date', 'Tue, 13 Aug 2019 16:34:18 GMT'), ('Connection', 'close'), ('Content-Length', '590')]
            content = [{'localId': 88, 'id': '5b8dc8cb-c8cb-c8cb-c8cb-c8cb39e6c8cb', 'name': 'Duplicate Profile', 'treeLocation': [{'id': 'ffffffff-0000-0000-0000-000000000000', 'name': 'APM Profiles'}, {'id': '1918e33f-a7f5-469a-8c2d-310b506ab797', 'name': 'Standard Library Profiles'}, {'id': 'e3ae6cb3-8200-487d-9ebd-8fd6cd68b6b2', 'name': 'Efficiency'}, {'id': 'a1d76ee9-ec62-4cd0-bb53-9cc92228f13b', 'name': 'Block-Cost Model'}], 'library': True, 'currentVersion': 9}, {'localId': 108, 'id': '12e212e2-12e2-12e2-12e2-ad12e2a14acc', 'name': 'Single Real Profile 2', 'treeLocation': [{'id': 'ffffffff-0000-0000-0000-000000000000', 'name': 'APM Profiles'}, {'id': '1918e33f-a7f5-469a-8c2d-310b506ab797', 'name': 'Standard Library Profiles'}, {'id': 'e3ae6cb3-8200-487d-9ebd-8fd6cd68b6b2', 'name': 'Efficiency'}, {'id': 'a1d76ee9-ec62-4cd0-bb53-9cc92228f13b', 'name': 'Block-Cost Model'}], 'library': True, 'currentVersion': 9}, {'localId': 56, 'id': 'f163eeee-63ee-63ee-63ee-1b363eed63ee', 'name': 'Single Profile 3', 'treeLocation': [{'id': 'ffffffff-0000-0000-0000-000000000000', 'name': 'APM Profiles'}, {'id': '1918e33f-a7f5-469a-8c2d-310b506ab797', 'name': 'Standard Library Profiles'}, {'id': 'e3ae6cb3-8200-487d-9ebd-8fd6cd68b6b2', 'name': 'Efficiency'}, {'id': 'a1d76ee9-ec62-4cd0-bb53-9cc92228f13b', 'name': 'Block-Cost Model'}], 'library': True, 'currentVersion': 8}, {'localId': 99, 'id': 'c152c3dd-496a-496a-496a-bd5fc3ddbd5f', 'name': 'Single Real Profile', 'treeLocation': [{'id': 'ffffffff-0000-0000-0000-000000000000', 'name': 'APM Profiles'}, {'id': '1918e33f-a7f5-469a-8c2d-310b506ab797', 'name': 'Standard Library Profiles'}, {'id': 'e3ae6cb3-8200-487d-9ebd-8fd6cd68b6b2', 'name': 'Efficiency'}, {'id': 'a1d76ee9-ec62-4cd0-bb53-9cc92228f13b', 'name': 'Block-Cost Model'}], 'library': True, 'currentVersion': 8}, {'localId': 500000, 'id': '5b8d6db7-c8cb-474f-b951-4c8e39e6eba1', 'name': 'Duplicate Profile', 'treeLocation': [{'id': 'ffffffff-0000-0000-0000-000000000000', 'name': 'APM Profiles'}, {'id': '1918e33f-a7f5-469a-8c2d-310b506ab797', 'name': 'Standard Library Profiles'}, {'id': 'e3ae6cb3-8200-487d-9ebd-8fd6cd68b6b2', 'name': 'Efficiency'}, {'id': 'a1d76ee9-ec62-4cd0-bb53-9cc92228f13b', 'name': 'Block-Cost Model'}], 'library': True, 'currentVersion': 10}]

        return resp_h, content

def print_resp(resp):
    for r in resp:
        pp.pprint(r)