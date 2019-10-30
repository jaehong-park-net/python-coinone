import time
import unittest
import uuid

from pycoinone.response import (
    PendingOrder,
    CompleteOrder,
    Response
)


class ResponseV2Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_response(self):
        res = Response({
            "result": "success",
            "errorCode": 0
        })
        self.assertEqual(res.result, "success")
        self.assertEqual(res.error_code, 0)

        res = Response({
            "result": "error",
            "errorCode": 1
        })
        self.assertEqual(res.result, "error")
        self.assertEqual(res.error_code, 1)

    def test_limit_order(self):
        uid = str(uuid.uuid4())
        timestamp = int(time.time())
        type = "bid"
        price = 10000.0
        quantity = 1.0
        fee_rate = 0.01
        index = 1

        order = PendingOrder({
            "orderId": uid,
            "timestamp": timestamp,
            "type": type,
            "price": price,
            "qty": quantity,
            "feeRate": fee_rate,
            "index": index
        })

        self.assertEqual(order.order_id, uid)
        self.assertEqual(order.timestamp, timestamp)
        self.assertEqual(order.type, type)
        self.assertEqual(order.price, price)
        self.assertEqual(order.quantity, quantity)
        self.assertEqual(order.fee_rate, fee_rate)
        self.assertEqual(order.index, index)

    def test_complete_order(self):
        uid = str(uuid.uuid4())
        timestamp = int(time.time())
        type = "bid"
        price = 10000.0
        quantity = 1.0
        fee_rate = 0.01
        fee = 0.01

        order = CompleteOrder({
            "orderId": uid,
            "timestamp": timestamp,
            "type": type,
            "price": price,
            "qty": quantity,
            "feeRate": fee_rate,
            "fee": fee
        })

        self.assertEqual(order.order_id, uid)
        self.assertEqual(order.timestamp, timestamp)
        self.assertEqual(order.type, type)
        self.assertEqual(order.price, price)
        self.assertEqual(order.quantity, quantity)
        self.assertEqual(order.fee_rate, fee_rate)
        self.assertEqual(order.fee, fee)

    @unittest.skip("To use to print.")
    def test_print_currencies(self):
        from pycoinone.response.test import SAMPLE_BALANCE_RESPONSE

        currencies = []
        for c in SAMPLE_BALANCE_RESPONSE.keys():
            currencies.append(c)
        currencies.remove("result")
        currencies.remove("errorCode")
        currencies.remove("normalWallets")

        print(currencies)


if __name__ == "__main__":
    unittest.main()
