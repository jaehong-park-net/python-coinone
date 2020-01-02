from pycoinone.session import CoinoneSession


class SessionV1(CoinoneSession):
    def __init__(self, access_token):
        super(SessionV1, self).__init__()
        self._access_token = access_token

    def get(self, url):
        return self._session.get(url, params={"access_token": self._access_token})

    def post(self, url, data=None):
        encoded_data = self._encode_data(data)

        return self._session.post(
            url,
            data=encoded_data,
            headers={'CONTENT-TYPE': 'application/x-www-form-urlencoded'}
        )

    def _encode_data(self, data):
        encoded_data = dict()
        encoded_data["access_token"] = self._access_token

        data = data or {}
        encoded_data.update(data)

        return encoded_data
