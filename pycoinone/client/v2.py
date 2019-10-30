from pycoinone.client import CoinoneClient
from pycoinone.client import NoAuthorizationError
from pycoinone.client import coinone_api_request
from pycoinone.session.v2 import SessionV2 as Session


def required_authorization(func):
    def _required_authorization(self, *args, **kwargs):
        access_token = self._access_token
        secret_key = self._secret_key
        if access_token is "" or secret_key is "":
            raise NoAuthorizationError()

        return func(self, *args, **kwargs)

    return _required_authorization


class ClientV2(CoinoneClient):
    API_VERSION = 'v2'

    # Private URLs
    USER_INFO_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/account/user_info'  # https://api.coinone.co.kr/v2/account/user_info
    BALANCE_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/account/balance'  # https://api.coinone.co.kr/v2/account/balance
    BUY_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/limit_buy'  # https://api.coinone.co.kr/v2/order/limit_buy
    SELL_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/limit_sell'  # https://api.coinone.co.kr/v2/order/limit_sell
    PENDING_ORDER_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/limit_orders'  # https://api.coinone.co.kr/v2/order/limit_orders
    COMPLETE_ORDER_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/complete_orders'  # https://api.coinone.co.kr/v2/order/complete_orders
    CANCEL_ORDER_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/cancel'  # https://api.coinone.co.kr/v2/order/cancel

    # Public URLs
    ORDER_URL = CoinoneClient.BASE_URL + '/orderbook'  # https://api.coinone.co.kr/orderbook
    TRADE_URL = CoinoneClient.BASE_URL + '/trades'  # https://api.coinone.co.kr/trades

    def __init__(self, access_token="", secret_key=""):
        super(ClientV2, self).__init__()
        self._access_token = access_token
        self._secret_key = secret_key
        self._session = Session(access_token, secret_key)

    @coinone_api_request
    def get_trades(self):
        res = self._session.get(
            ClientV2.TRADE_URL
        )

        return res

    @coinone_api_request
    def get_orders(self):
        res = self._session.get(
            ClientV2.ORDER_URL
        )

        return res

    @coinone_api_request
    @required_authorization
    def buy(self, price, quantity, currency="btc"):
        res = self._session.post(
            ClientV2.BUY_URL,
            {
                "price": price,
                "qty": quantity,
                "currency": currency
            }
        )

        return res

    @coinone_api_request
    @required_authorization
    def sell(self, price, quantity, currency="btc"):
        res = self._session.post(
            ClientV2.SELL_URL,
            {
                "price": price,
                "qty": quantity,
                "currency": currency
            }
        )

        return res

    @coinone_api_request
    @required_authorization
    def get_user_info(self):
        res = self._session.post(
            ClientV2.USER_INFO_URL
        )

        return res

    @coinone_api_request
    @required_authorization
    def get_balance(self):
        res = self._session.post(
            ClientV2.BALANCE_URL
        )

        return res

    @coinone_api_request
    @required_authorization
    def get_pending_orders(self, currency="btc"):
        res = self._session.post(
            ClientV2.PENDING_ORDER_URL,
            {"currency": currency}
        )

        return res

    @coinone_api_request
    @required_authorization
    def get_complete_orders(self, currency="btc"):
        res = self._session.post(
            ClientV2.COMPLETE_ORDER_URL,
            {"currency": currency}
        )

        return res

    @coinone_api_request
    @required_authorization
    def cancel_order(self, order, currency="btc"):
        """
        
        :param order: PendingOrdersResponse
        :param currency: str
        :return: Response
        """
        res = self._session.post(
            ClientV2.CANCEL_ORDER_URL,
            {
                "order_id": order.order_id,
                "price": order.price,
                "qty": order.quantity,
                "is_ask": 1 if order.type == "ask" else 0,
                "currency": currency
            }
        )

        return res
