from pycoinone.client import CoinoneClient
from pycoinone.client import NoAuthorizationError
from pycoinone.client import coinone_api_request
from pycoinone.session.v1 import SessionV1 as Session


def required_authorization(func):
    def _required_authorization(self, *args, **kwargs):
        access_token = self._access_token
        if access_token is "":
            raise NoAuthorizationError()

        return func(self, *args, **kwargs)

    return _required_authorization


class ClientV1(CoinoneClient):
    API_VERSION = 'v1'

    # Private URLs
    USER_INFO_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/account/user_info'  # https://api.coinone.co.kr/v1/account/user_info
    BALANCE_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/account/balance'  # https://api.coinone.co.kr/v1/account/balance
    BUY_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/limit_buy'  # https://api.coinone.co.kr/v1/order/limit_buy
    SELL_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/limit_sell'  # https://api.coinone.co.kr/v1/order/limit_sell
    PENDING_ORDER_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/limit_orders'  # https://api.coinone.co.kr/v1/order/limit_orders
    COMPLETE_ORDER_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/complete_orders'  # https://api.coinone.co.kr/v1/order/complete_orders
    CANCEL_ORDER_URL = CoinoneClient.BASE_URL + '/' + API_VERSION + '/order/cancel'  # https://api.coinone.co.kr/v1/order/cancel

    # Public URLs
    ORDER_URL = CoinoneClient.BASE_URL + '/orderbook'  # https://api.coinone.co.kr/orderbook
    TRADE_URL = CoinoneClient.BASE_URL + '/trades'  # https://api.coinone.co.kr/trades

    def __init__(self, access_token=""):
        super(ClientV1, self).__init__()
        self._access_token = access_token
        self._session = Session(access_token)

    @coinone_api_request
    def get_trades(self):
        """
        Get trades.
        :return: TradeResponse
        """
        res = self._session._session.get(
            ClientV1.TRADE_URL
        )

        return res

    @coinone_api_request
    def get_orders(self):
        """
        Get orders.
        :return: OrderResponse
        """
        res = self._session._session.get(
            ClientV1.ORDER_URL
        )

        return res

    @coinone_api_request
    @required_authorization
    def get_user_info(self):
        """
        Get user information.
        :return: UserInfoResponse
        """
        res = self._session.get(
            ClientV1.USER_INFO_URL
        )

        return res

    @coinone_api_request
    @required_authorization
    def get_balance(self):
        """
        Get balance
        :return: BalanceResponse
        """
        res = self._session.get(
            ClientV1.BALANCE_URL
        )

        return res

    @coinone_api_request
    @required_authorization
    def get_pending_orders(self):
        """
        Get pending orders.
        :return: PendingOrderResponse
        """
        res = self._session.get(
            ClientV1.PENDING_ORDER_URL,
        )

        return res

    @coinone_api_request
    @required_authorization
    def get_complete_orders(self):
        """
        Get complete orders.
        :return: CompleteOrderResponse
        """
        res = self._session.get(
            ClientV1.COMPLETE_ORDER_URL,
        )

        return res

    @coinone_api_request
    @required_authorization
    def cancel_order(self, order):
        """
        Cancel order.
        :param order: PendingOrder
        :return: Response
        """
        res = self._session.post(
            ClientV1.CANCEL_ORDER_URL,
            {
                "order_id": order.order_id,
                "price": order.price,
                "qty": order.quantity,
                "is_ask": 1 if order.type == "ask" else 0,
            }
        )

        return res

    @coinone_api_request
    @required_authorization
    def buy(self, price, quantity):
        """
        Buy.
        :param price: float
        :param quantity: float
        :return: LimitOrderResponse
        """
        res = self._session.post(
            ClientV1.BUY_URL,
            {
                "price": price,
                "qty": quantity
            }
        )

        return res

    @coinone_api_request
    @required_authorization
    def sell(self, price, quantity):
        """
        Sell.
        :param price: float
        :param quantity: float
        :return: LimitOrderResponse
        """
        res = self._session.post(
            ClientV1.SELL_URL,
            {
                "price": price,
                "qty": quantity
            }
        )

        return res
