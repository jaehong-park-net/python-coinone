import requests


class CoinoneSession(object):
    def __init__(self):
        self._session = requests.Session()
