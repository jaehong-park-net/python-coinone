from functools import cmp_to_key

ERROR_MESSAGE = {
    1: "Blocked user access.",
    8: "Request Token Parameter is needed."
}

CURRENCIES = (
    'add', 'adt', 'amo', 'black', 'btc', 'chl', 'cpt', 'dappt', 'egg', 'enj', 'eox', 'eth', 'luna', 'ong',
    'ont', 'orbs', 'pxl', 'hint', 'wecash', 'xtz', 'storj', 'storm', 'zil', 'cosm', 'dad', 'ksc', 'gas', 'xlm',
    'atom', 'spin', 'bat', 'loom', 'iota', 'trx', 'tfuel', 'gno', 'btt', 'edna', 'pib', 'krw', 'btg', 'matic',
    'lamb', 'neo', 'rep', 'abl', 'celr', 'zrx', 'prom', 'theta', 'xrp', 'credo', 'omg', 'horus', 'bsv', 'snm',
    'ankr', 'vnt', 'data', 'mzk', 'atd', 'bch', 'qtum', 'knc', 'eos', 'etc', 'temco', 'ltc'
)


class Raw(object):
    def __init__(self, raw):
        self._raw = raw

    def __getattr__(self, item):
        return self._raw.get(item, None)


class ResponseBase(Raw):
    """
    On success:

        {
            "result": "success",
            "errorCode": "0",
            ...
            ...
            ...
        }


    On error:

        {
            "result": "error",
            "errorCode": "<int:error_code>",
        }


    Error Codes:
        4       Blocked user access
        8       Request Token Parameter is needed
        11	    Access token is missing
        12	    Invalid access token
        40	    Invalid API permission
        51	    Invalid API
        53	    Two Factor Auth Fail
        101	    Invalid format
        103	    Lack of Balance
        104	    Order id is not exist
        105	    Price is not correct
        107	    Parameter error
        113	    Quantity is too low(ETH, ETC > 0.01)
        114	    This is not a valid your order amount.
        120	    V2 API payload is missing
        121	    V2 API signature is missing
        122	    V2 API nonce is missing
        123	    V2 API signature is not correct
        130	    V2 API Nonce value must be a positive integer
        131	    V2 API Nonce is must be bigger then last nonce
        132	    V2 API body is corrupted
        150	    It's V1 API. V2 Access token is not acceptable
        151	    It's V2 API. V1 Access token is not acceptable
        152	    Invalid address
        153	    The address is detected by FDS. Please contact our customer center.
        405	    Server error
        1201    API Deprecated
        1206    User not found
        11003   Unknown cryptocurrency.
        11014   The service is temporarily not offered.
        11015   The order limit price cancellation denied.
        11016   The order cancellation denied.
        11017   This is not a valid input value.
        11025   The cryptocurrency is not supported.
        11062   This is not a valid the fund-raising period of time.
        11063   This is not a valid the fund-raising amount.
        11064   It has not been fundraising information.
        11065   It is not the fundraiser now.
        11066   The fundraising has been done.
        11067   The fundraising has been done for goal amount.
        11074   This is not a valid your ID.
        11075   For the safe trading environment, orders are limited for a notified period of time.
        11076   For the safe trading environment, sell orders can be placed after a notified period of time.
        11077   For the safe trading environment, buy orders can be placed after a notified period of time.
        11078   For the safe trading environment, sell orders below the certain price criteria notified are limited.
        11079   For the safe trading environment, sell orders above the certain price criteria notified are limited.
        11080   For the safe trading environment, buy orders below the certain price criteria notified are limited.
        11081   For the safe trading environment, buy orders above the certain price criteria notified are limited.
        11082   The order quantity is non-cancelable.
        11083   Your order amount is less than minimum amount.(500 KRW)
    """

    __attributes__ = [
        "result",
        "errorCode"
    ]

    def __init__(self, raw):
        super(ResponseBase, self).__init__(raw)

    @property
    def result(self):
        return self._raw.get("result")

    @property
    def error_code(self):
        return int(self._raw.get("errorCode"))


def make_response_key(res):
    def list_str_cmp(x, y):
        if isinstance(x, dict) and isinstance(y, str) \
                or isinstance(x, str) and isinstance(y, dict):
            return 1 if isinstance(x, dict) else -1

        return 0 if x == y else 1 if x > y else -1

    res = sorted(res, key=cmp_to_key(list_str_cmp))
    key = tuple()
    for r in res:
        if isinstance(r, dict):
            for k, v in r.items():
                sub_key = make_response_key(v)
                key += ((k, sub_key),)
        else:
            key += (r,)

    return key


class ResponseFactory(object):
    MAP = dict()

    @staticmethod
    def create(res):
        # Exceptional create
        if res.get("normalWallets") is not None:
            return BalanceResponse(res)

        key = make_response_key(res)
        response_class = ResponseFactory.MAP[key]

        return response_class(res)


def coinone_api_response(cls):
    # key = make_response_key(cls.__attributes__ + cls.__bases__[0].__attributes__)
    key = make_response_key(cls.__attributes__)
    ResponseFactory.MAP[key] = cls

    return cls


@coinone_api_response
class Response(ResponseBase):
    pass


class Trade(Raw):
    @property
    def type(self):
        return "ask" if self._raw.get("is_ask") == "1" else "bid"

    @property
    def timestamp(self):
        return int(self._raw.get("timestamp"))

    @property
    def price(self):
        return float(self._raw.get("price"))

    @property
    def id(self):
        return int(self._raw.get("id"))

    @property
    def quantity(self):
        return float(self._raw.get("qty"))


@coinone_api_response
class TradeResponse(Response):
    __attributes__ = [
        "result",
        "errorCode",
        "timestamp",
        "completeOrders",
        "currency"
    ]

    def __init__(self, raw):
        super(TradeResponse, self).__init__(raw)

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        try:
            order = self._raw.get("completeOrders")[self._i]
            self._i += 1
        except IndexError:
            raise StopIteration

        return Trade(order)

    def __len__(self):
        return len(self._raw.get("completeOrders"))

    def __getitem__(self, item):
        return Trade(self._raw.get("completeOrders")[item])


class Ask(Raw):
    @property
    def price(self):
        return float(self._raw.get("price"))

    @property
    def quantity(self):
        return float(self._raw.get("qty"))


class Bid(Raw):
    @property
    def price(self):
        return float(self._raw.get("price"))

    @property
    def quantity(self):
        return float(self._raw.get("qty"))


@coinone_api_response
class OrderResponse(Response):
    __attributes__ = [
        "result",
        "errorCode",
        "timestamp",
        "currency",
        "ask",
        "bid"
    ]

    def __init__(self, raw):
        super(OrderResponse, self).__init__(raw)

    @property
    def asks(self):
        return OrderResponse.Asks(self._raw.get("ask"))

    @property
    def bids(self):
        return OrderResponse.Asks(self._raw.get("bid"))

    class Asks(Raw):
        def __init__(self, raw):
            super(OrderResponse.Asks, self).__init__(raw)

        def __len__(self):
            return len(self._raw)

        def __iter__(self):
            self._i = 0
            return self

        def __next__(self):
            try:
                ask = self._raw[self._i]
                self._i += 1
            except IndexError:
                raise StopIteration

            return Ask(ask)

        def __getitem__(self, item):
            return Ask(self._raw[item])

    class Bids(Raw):
        def __init__(self, raw):
            super(OrderResponse.Bids, self).__init__(raw)

        def __len__(self):
            return len(self._raw)

        def __iter__(self):
            self._i = 0
            return self

        def __next__(self):
            try:
                bid = self._raw[self._i]
                self._i += 1
            except IndexError:
                raise StopIteration

            return Bid(bid)

        def __getitem__(self, item):
            return Bid(self._raw[item])


class Order(Raw):
    __attributes__ = [
        "orderId",
        "timestamp",
        "type",
        "price",
        "qty",
        "feeRate"
    ]

    def __init__(self, raw):
        super(Order, self).__init__(raw)

    def __eq__(self, other):
        return self.order_id == other.order_id \
               and self.timestamp == other.timestamp \
               and self.price == other.price \
               and self.quantity == other.quantity

    def __hash__(self):
        return hash(self.order_id)

    def __str__(self):
        return \
            "order_id={order_id}\n" \
            "timestamp={timestamp}\n" \
            "type={type}\n" \
            "price={price}\n" \
            "quantity={quantity}\n" \
            "fee_rate={fee_rate}\n".format(
                order_id=self.order_id,
                timestamp=self.timestamp,
                type=self.type,
                price=self.price,
                quantity=self.quantity,
                fee_rate=self.fee_rate
            )

    @property
    def order_id(self):
        return self._raw.get("orderId")

    @property
    def timestamp(self):
        return int(self._raw.get("timestamp"))

    @property
    def type(self):
        return self._raw.get("type")

    @property
    def price(self):
        return float(self._raw.get("price"))

    @property
    def quantity(self):
        return float(self._raw.get("qty"))

    @property
    def fee_rate(self):
        return float(self._raw.get("feeRate"))


@coinone_api_response
class UserInfoResponse(Response):
    __attributes__ = [
        "errorCode",
        "result",
        "userInfo"
    ]

    def __init__(self, raw):
        super(UserInfoResponse, self).__init__(raw)

    def __getattr__(self, item):
        return self._raw.get("userInfo").get(item)

    class MobileInfo(Raw):
        def __init__(self, raw):
            super(UserInfoResponse.MobileInfo, self).__init__(raw)

        def __getattr__(self, item):
            return self._raw.get(item)


class Balance(Raw):
    def __init__(self, raw):
        super(Balance, self).__init__(raw)

    @property
    def avail(self):
        return float(self._raw.get("avail"))

    @property
    def balance(self):
        return float(self._raw.get("balance"))


@coinone_api_response
class BalanceResponse(Response):
    __attributes__ = [
        "result",
        "errorCode",
        "normalWallets"
    ]

    def __init__(self, raw):
        super(BalanceResponse, self).__init__(raw)

    def __getattr__(self, item):
        if item in CURRENCIES:
            return Balance(self._raw.get(item))
        else:
            raise AttributeError("There is not such currency.")


class PendingOrder(Order):
    """
    Raw structure

    {
        "orderId": <uuid:uuid>,
        "timestamp": <int:timestamp>,
        "type": <string:<ask|bid>>,
        "price": <float:price>,
        "qty": <float:quantity>,
        "feeRate": <float:fee_rate>,
        "index": <int:index>
    }
    """

    def __init__(self, raw):
        super(PendingOrder, self).__init__(raw)

    @property
    def index(self):
        return int(self._raw.get("index"))


class CompleteOrder(Order):
    """
    Raw structure

    {
        "orderId": <uuid:uuid>,
        "timestamp": <int:timestamp>,
        "type": <string:<ask|bid>>,
        "price": <float:price>,
        "qty": <float:quantity>,
        "feeRate": <float:fee_rate>,
        "fee": <float:index>
    }
    """

    def __init__(self, raw):
        super(CompleteOrder, self).__init__(raw)

    @property
    def fee(self):
        return float(self._raw.get("fee"))


@coinone_api_response
class LimitOrderResponse(Response):
    """
    {
        "result": "success",
        "errorCode": "0",
        "orderId": "8a82c561-40b4-4cb3-9bc0-9ac9ffc1d63b"
    }
    """
    __attributes__ = [
        "result",
        "errorCode",
        "orderId"
    ]

    def __init__(self, raw):
        super(LimitOrderResponse, self).__init__(raw)

    @property
    def order_id(self):
        return self._raw.get("orderId")


@coinone_api_response
class PendingOrdersResponse(Response):
    """
    {
        "result": "success",
        "errorCode": "0",
        "limitOrders": [
            {
                "index": "0",
                "orderId": "68665943-1eb5-4e4b-9d76-845fc54f5489",
                "timestamp": "1449037367",
                "price": "444000.0",
                "qty": "0.3456",
                "type": "ask",
                "feeRate": "-0.0015"
            }
        ]
    }
    """
    __attributes__ = [
        "result",
        "errorCode",
        "limitOrders"
    ]

    def __init__(self, raw):
        super(PendingOrdersResponse, self).__init__(raw)

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        try:
            order = self._raw.get("limitOrders")[self._i]
            self._i += 1
        except IndexError:
            raise StopIteration

        return PendingOrder(order)

    def __len__(self):
        return len(self._raw.get("limitOrders"))

    def __getitem__(self, item):
        return PendingOrder(self._raw.get("limitOrders")[item])


@coinone_api_response
class CompleteOrdersResponse(Response):
    """
    {
        "result": "success",
        "errorCode": "0",
        "completeOrders": [
            {
                "timestamp": "1416561032",
                "price": "419000.0",
                "type": "bid",
                "qty": "0.001",
                "feeRate": "-0.0015",
                "fee": "-0.0000015",
                "orderId": "E84A1AC2-8088-4FA0-B093-A3BCDB9B3C85"
            }
        ]
    }
    """
    __attributes__ = [
        "result",
        "errorCode",
        "completeOrders"
    ]

    def __init__(self, raw):
        super(CompleteOrdersResponse, self).__init__(raw)

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        try:
            order = self._raw.get("completeOrders")[self._i]
            self._i += 1
        except IndexError:
            raise StopIteration

        return CompleteOrder(order)

    def __len__(self):
        return len(self._raw.get("completeOrders"))

    def __getitem__(self, item):
        return CompleteOrder(self._raw.get("completeOrders")[item])
