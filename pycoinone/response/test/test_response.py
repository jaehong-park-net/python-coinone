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

    def test_response_factory(self):
        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0"
        })
        self.assertIsInstance(res, Response)

        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "timestamp": "123456789",
            "currency": "btc",
            "ask": [],
            "bid": []
        })
        self.assertIsInstance(res, OrderResponse)

        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "timestamp": "123456789",
            "completeOrders": [],
            "currency": "btc"
        })
        self.assertIsInstance(res, TradeResponse)

        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "userInfo": {}
        })
        self.assertIsInstance(res, UserInfoResponse)

        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "normalWallets": {}
        })
        self.assertIsInstance(res, BalanceResponse)

        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "orderId": "8a82c561-40b4-4cb3-9bc0-9ac9ffc1d63b"
        })
        self.assertIsInstance(res, LimitOrderResponse)

        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "limitOrders": []
        })
        self.assertIsInstance(res, PendingOrdersResponse)

        res = ResponseFactory.create({
            "result": "success",
            "errorCode": "0",
            "completeOrders": []
        })
        self.assertIsInstance(res, CompleteOrdersResponse)


if __name__ == "__main__":
    unittest.main()
