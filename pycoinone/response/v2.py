from pycoinone.response import (
    coinone_api_response,
    UserInfoResponse,
    BalanceResponse,
    LimitOrderResponse,
    PendingOrdersResponse,
    CompleteOrdersResponse
)


@coinone_api_response
class UserInfoResponseV2(UserInfoResponse):
    """
    {
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
            "securityLevel": "4",
            "feeRate": {
                "btc": {
                    "maker": "0.001",
                    "taker": "0.001"
                },
                "bch": {
                    "maker": "0.001",
                    "taker": "0.001"
                },
                "eth": {
                    "maker": "0.001",
                    "taker": "0.001"
                }
            }
        }
    }
    """
    pass


@coinone_api_response
class BalanceResponseV2(BalanceResponse):
    """ 
    {
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
    }
    """
    pass


@coinone_api_response
class LimitOrderResponseV2(LimitOrderResponse):
    """
    {
        "result": "success",
        "errorCode": "0",
        "orderId": "8a82c561-40b4-4cb3-9bc0-9ac9ffc1d63b"
    }
    """
    pass


@coinone_api_response
class PendingOrdersResponseV2(PendingOrdersResponse):
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
    pass


@coinone_api_response
class CompleteOrdersResponseV2(CompleteOrdersResponse):
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
    pass
