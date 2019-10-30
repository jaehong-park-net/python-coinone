import json
import time

import base64
import hashlib
import hmac

from pycoinone.session import CoinoneSession


class SessionV2(CoinoneSession):
    def __init__(self, access_token, secret_key):
        super(SessionV2, self).__init__()
        self._access_token = access_token
        self._secret_key = secret_key

    def get(self, url):
        return self._session.get(url)

    def post(self, url, data=None):
        encoded_data = self._encode_data(data)
        encoded_header = self._encode_header(encoded_data)

        return self._session.post(url, encoded_data, headers=encoded_header)

    def _encode_data(self, data):
        encoded_data = dict()
        encoded_data["access_token"] = self._access_token
        encoded_data["nonce"] = int(time.time() * 1000)

        data = data or {}
        for k, v in data.items():
            encoded_data[k] = v

        encoded_data = json.dumps(encoded_data).encode()
        encoded_data = base64.b64encode(encoded_data)

        return encoded_data

    def _encode_header(self, data):
        encoded_secret_key = self._secret_key.encode()

        encoded_header = dict()
        encoded_header["CONTENT-TYPE"] = "application/json"
        encoded_header["X-COINONE-PAYLOAD"] = data
        encoded_header["X-COINONE-SIGNATURE"] = hmac.new(encoded_secret_key, data, hashlib.sha512).hexdigest()

        return encoded_header
