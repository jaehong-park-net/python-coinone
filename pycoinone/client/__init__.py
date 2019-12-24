import json

from requests import HTTPError
from requests.exceptions import ConnectionError

from pycoinone.response import ResponseFactory


class NoAuthorizationError(Exception):
    pass


class ResponseError(Exception):
    pass


def coinone_api_request(func):
    def _may_raise_exception(self, *args, **kwargs):

        try:
            res = func(self, *args, **kwargs)
        except HTTPError:
            raise ResponseError("Python request http error occured.")
        except ConnectionError:
            raise ResponseError("Python requests connection error occured.")

        status_code = res.status_code
        if status_code != 200:
            raise ResponseError()

        text = res.text
        data = json.loads(text)
        coinone_result = data.get("result")
        coinone_error_code = int(data.get("errorCode"))
        if coinone_result != "success":
            raise ResponseError("Result was not successful. coinone error code is {}.".format(coinone_error_code))
        if coinone_error_code != 0:
            raise ResponseError("Result was successful. But coinone error code is {}.".format(coinone_error_code))

        return ResponseFactory.create(data)

    return _may_raise_exception


class CoinoneClient(object):
    BASE_URL = 'https://api.coinone.co.kr'
