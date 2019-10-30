import unittest
from unittest import mock

import os

from pycoinone.client import NoAuthorizationError
from pycoinone.client.test import mock_request as request
from pycoinone.client.v1 import ClientV1 as Client


def required_v1_authorization_test(func):
    def _required_authorization_test(self):
        access_token = os.environ.get("COINONE_V1_ACCESS_TOKEN", None)
        if access_token is None:
            raise unittest.SkipTest("Required to be set env variables 'COINONE_V1_ACCESS_TOKEN'.")

        return func(self, access_token)

    return _required_authorization_test


class CoinoneClientV1Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_client_without_auth(self):
        client = Client()

        self.assertRaises(NoAuthorizationError, client.get_user_info)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_get_trades_with_mock(self, mock_request):
        _ = mock_request

        client = Client()

        trades = client.get_trades()
        for trade in trades:
            self.assertIsInstance(trade.id, int)
            self.assertIsInstance(trade.type, str)
            self.assertIsInstance(trade.timestamp, int)
            self.assertIsInstance(trade.price, float)
            self.assertIsInstance(trade.quantity, float)

    def test_get_trades(self):
        client = Client()

        trades = client.get_trades()
        for trade in trades:
            self.assertIsInstance(trade.id, int)
            self.assertIsInstance(trade.type, str)
            self.assertIsInstance(trade.timestamp, int)
            self.assertIsInstance(trade.price, float)
            self.assertIsInstance(trade.quantity, float)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_get_orders_with_mock(self, mock_request):
        _ = mock_request

        client = Client()

        orders = client.get_orders()
        for ask in orders.asks:
            self.assertIsInstance(ask.price, float)
            self.assertIsInstance(ask.quantity, float)
        for bid in orders.bids:
            self.assertIsInstance(bid.price, float)
            self.assertIsInstance(bid.quantity, float)

    def test_get_orders(self):
        client = Client()

        orders = client.get_orders()
        for ask in orders.asks:
            self.assertIsInstance(ask.price, float)
            self.assertIsInstance(ask.quantity, float)
        for bid in orders.bids:
            self.assertIsInstance(bid.price, float)
            self.assertIsInstance(bid.quantity, float)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_get_user_info_with_mock(self, mock_request):
        _ = mock_request

        client = Client("access_token")

        user_info = client.get_user_info()
        self.assertIsInstance(user_info.mobileInfo["userName"], str)
        self.assertIsInstance(user_info.mobileInfo["phoneNumber"], str)
        self.assertIsInstance(user_info.bankInfo["depositor"], str)
        self.assertIsInstance(user_info.bankInfo["accountNumber"], str)
        self.assertIsInstance(user_info.emailInfo["email"], str)

    @required_v1_authorization_test
    def test_get_user_info(self, access_token):
        client = Client(access_token)

        user_info = client.get_user_info()
        self.assertIsInstance(user_info.mobileInfo["userName"], str)
        self.assertIsInstance(user_info.mobileInfo["phoneNumber"], str)
        self.assertIsInstance(user_info.bankInfo["depositor"], str)
        self.assertIsInstance(user_info.bankInfo["accountNumber"], str)
        self.assertIsInstance(user_info.emailInfo["email"], str)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_get_balance_with_mock(self, mock_request):
        _ = mock_request

        client = Client("access_token")

        balance = client.get_balance()
        self.assertIsInstance(balance.btc.balance, float)
        self.assertIsInstance(balance.krw.balance, float)
        self.assertIsInstance(balance.btg.balance, float)

    @required_v1_authorization_test
    def test_get_balance(self, access_token):
        client = Client(access_token)

        balance = client.get_balance()
        self.assertIsInstance(balance.btc.balance, float)
        self.assertIsInstance(balance.krw.balance, float)
        self.assertIsInstance(balance.btg.balance, float)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_get_pending_orders_with_mock(self, mock_request):
        _ = mock_request

        client = Client("access_token")

        orders = client.get_pending_orders()
        for order in orders:
            self.assertIsInstance(order.order_id, str)
            self.assertIsInstance(order.timestamp, int)
            self.assertIsInstance(order.type, str)
            self.assertIsInstance(order.price, float)
            self.assertIsInstance(order.quantity, float)
            self.assertIsInstance(order.fee_rate, float)
            self.assertIsInstance(order.index, int)

    @required_v1_authorization_test
    def test_get_pending_orders(self, access_token):
        client = Client(access_token)

        orders = client.get_pending_orders()
        for order in orders:
            self.assertIsInstance(order.order_id, str)
            self.assertIsInstance(order.timestamp, int)
            self.assertIsInstance(order.type, str)
            self.assertIsInstance(order.price, float)
            self.assertIsInstance(order.quantity, float)
            self.assertIsInstance(order.fee_rate, float)
            self.assertIsInstance(order.index, int)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_get_complete_orders_with_mock(self, mock_request):
        _ = mock_request

        client = Client("access_token")

        orders = client.get_complete_orders()
        for order in orders:
            self.assertIsInstance(order.order_id, str)
            self.assertIsInstance(order.timestamp, int)
            self.assertIsInstance(order.type, str)
            self.assertIsInstance(order.price, float)
            self.assertIsInstance(order.quantity, float)
            self.assertIsInstance(order.fee_rate, float)
            self.assertIsInstance(order.fee, float)

    @required_v1_authorization_test
    def test_get_complete_orders(self, access_token):
        client = Client(access_token)

        orders = client.get_complete_orders()
        for order in orders:
            self.assertIsInstance(order.order_id, str)
            self.assertIsInstance(order.timestamp, int)
            self.assertIsInstance(order.type, str)
            self.assertIsInstance(order.price, float)
            self.assertIsInstance(order.quantity, float)
            self.assertIsInstance(order.fee_rate, float)
            self.assertIsInstance(order.fee, float)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_cancel_order_with_mock(self, mock_request):
        _ = mock_request

        client = Client("access_token")

        orders = client.get_pending_orders()
        for order in orders:
            res = client.cancel_order(order)
            self.assertEqual(res.result, "success")
            self.assertEqual(res.error_code, 0)

    @required_v1_authorization_test
    def test_cancel_order(self, access_token):
        client = Client(access_token)

        orders = client.get_pending_orders()
        for order in orders:
            res = client.cancel_order(order)
            self.assertEqual(res.result, "success")
            self.assertEqual(res.error_code, 0)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_buy_with_mock(self, mock_request):
        _ = mock_request

        client = Client("access_token")
        order = client.buy(100000, 0.001)

        self.assertEqual(order.result, "success")
        self.assertEqual(order.error_code, 0)
        self.assertIsInstance(order.order_id, str)

    @unittest.skip("Dangerous to run!")
    @required_v1_authorization_test
    def test_buy(self, access_token):
        client = Client(access_token)
        order = client.buy(1000000, 0.001)

        self.assertEqual(order.result, "success")
        self.assertEqual(order.error_code, 0)
        self.assertIsInstance(order.order_id, str)

    @mock.patch("requests.Session.request", side_effect=request)
    def test_sell_with_mock(self, mock_request):
        _ = mock_request

        client = Client("access_token")
        order = client.sell(13000000, 0.001)

        self.assertEqual(order.result, "success")
        self.assertEqual(order.error_code, 0)
        self.assertIsInstance(order.order_id, str)

    @unittest.skip("Dangerous to run!")
    @required_v1_authorization_test
    def test_sell(self, access_token):
        client = Client(access_token)
        order = client.sell(13000000, 0.001)

        self.assertEqual(order.result, "success")
        self.assertEqual(order.error_code, 0)
        self.assertIsInstance(order.order_id, str)


if __name__ == "__main__":
    unittest.main()
