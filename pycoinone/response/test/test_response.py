import unittest

from pycoinone.response import (
    Response,
    OrderResponse,
    TradeResponse,
    UserInfoResponse,
    BalanceResponse,
    LimitOrderResponse,
    PendingOrdersResponse,
    CompleteOrdersResponse
)
from pycoinone.response import ResponseFactory


class ResponseTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_response_factory_default(self):
        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0"
        })
        self.assertIsInstance(res, Response)

    def test_response_factory_order(self):
        res = ResponseFactory.create({
            "errorCode": "0",
            "timestamp": "1416895635",
            "currency": "btc",
            "bid": [
                {
                    "price": "414000.0",
                    "qty": "11.4946"
                },
                {
                    "price": "414000.0",
                    "qty": "11.4946"
                }
            ],
            "ask": [
                {
                    "price": "414000.0",
                    "qty": "11.4946"
                },
                {
                    "price": "414000.0",
                    "qty": "11.4946"
                }
            ],
            "result": "success"
        })
        self.assertIsInstance(res, OrderResponse)

    def test_response_factory_trade(self):
        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "timestamp": "1416895635",
            "currency": "btc",
            "completeOrders": [
                {
                    "timestamp": "1416893212",
                    "price": "420000.0",
                    "qty": "0.1",
                    "is_ask": "1"
                }
            ]
        })
        self.assertIsInstance(res, TradeResponse)

    def test_response_factory_user_info(self):
        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "userInfo": {
                "virtualAccountInfo": {
                    "depositor": "John",
                    "accountNumber": "0123456789",
                    "bankName": "bankName"
                },
                "mobileInfo": {
                    "userName": "John",
                    "phoneNumber": "0123456789",
                    "phoneCorp": "1",
                    "isAuthenticated": "true"
                },
                "bankInfo": {
                    "depositor": "John",
                    "bankCode": "20",
                    "accountNumber": "0123456789",
                    "isAuthenticated": "true"
                },
                "emailInfo": {
                    "isAuthenticated": "true",
                    "email": "john@coinone.com"
                },
            }
        })
        self.assertIsInstance(res, UserInfoResponse)

    def test_response_factory_balance(self):
        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "normalWallets": [
                {
                    "balance": "6.1151",
                    "label": "First Wallet"
                },
                {
                    "balance": "6.9448",
                    "label": "Second Wallet"
                }
            ],
            "btc": {
                "avail": "344.33703699",
                "balance": "344.33703699"
            },
            "bch": {
                "avail": "1.00001234",
                "balance": "1.00001234"
            },
            "eth": {
                "avail": "1.00001234",
                "balance": "1.00001234"
            },
            "krw": {
                "avail": "6901425",
                "balance": "6901430"
            }
        })
        self.assertIsInstance(res, BalanceResponse)

    def test_response_factory_limit_order(self):
        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "orderId": "8a82c561-40b4-4cb3-9bc0-9ac9ffc1d63b"
        })
        self.assertIsInstance(res, LimitOrderResponse)

    def test_response_factory_pending_order(self):
        res = ResponseFactory.create({
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
        })
        self.assertIsInstance(res, PendingOrdersResponse)

    def test_response_factory_complete_order(self):
        res = ResponseFactory.create({
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
        })
        self.assertIsInstance(res, CompleteOrdersResponse)


if __name__ == "__main__":
    unittest.main()
