import json
from unittest.mock import MagicMock

MOCK_RESPONSE_MAP = {
    # Public
    "https://api.coinone.co.kr/trades": {
        "GET": {
            "result": "success",
            "errorCode": "0",
            "timestamp": "1571575244",
            "currency": "btc",
            "completeOrders": [
                {
                    "is_ask": "0",
                    "timestamp": "1572354513",
                    "price": "10917000.0",
                    "id": "1572354513000001",
                    "qty": "0.0555"
                },
                {
                    "is_ask": "1",
                    "timestamp": "1572354508",
                    "price": "10920000.0",
                    "id": "1572354508000002",
                    "qty": "0.0555"
                },
                {
                    "is_ask": "1",
                    "timestamp": "1572354508",
                    "price": "10920000.0",
                    "id": "1572354508000001",
                    "qty": "0.0912"
                },
                {
                    "is_ask": "1",
                    "timestamp": "1572354506",
                    "price": "10920000.0",
                    "id": "1572354506000001",
                    "qty": "0.0912"
                }
            ],
        }
    },
    "https://api.coinone.co.kr/orderbook": {
        "GET": {
            "result": "success",
            "errorCode": "0",
            "timestamp": "1571575244",
            "currency": "btc",
            "ask": [
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
            ],
            "bid": [
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
                {"price": "0.0", "qty": "0.0"},
            ]
        }
    },


    # V1 responses
    "https://api.coinone.co.kr/v1/account/user_info": {
        "GET": {
            "result": "success",
            "errorCode": "0",
            "userInfo": {
                "mobileInfo": {
                    "userName": "name",
                    "phoneNumber": "00000000000",
                    "phoneCorp": "0",
                },
                "bankInfo": {
                    "depositor": "name",
                    "accountNumber": "00000000000"
                },
                "emailInfo": {
                    "email": "email@email.email"
                }
            }
        }
    },
    "https://api.coinone.co.kr/v1/account/balance": {
        "GET": {
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
            "btg": {
                "avail": "1.00001234",
                "balance": "1.00001234"
            },
            "krw": {
                "avail": "6901425",
                "balance": "6901430"
            }
        }
    },
    "https://api.coinone.co.kr/v1/order/limit_orders": {
        "GET": {
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
    },
    "https://api.coinone.co.kr/v1/order/complete_orders": {
        "GET": {
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
    },
    "https://api.coinone.co.kr/v1/order/cancel": {
        "POST": {
            "result": "success",
            "errorCode": "0"
        }
    },
    "https://api.coinone.co.kr/v1/order/limit_buy": {
        "POST": {
            "result": "success",
            "errorCode": "0",
            "orderId": "8a82c561-40b4-4cb3-9bc0-9ac9ffc1d63b"
        }

    },
    "https://api.coinone.co.kr/v1/order/limit_sell": {
        "POST": {
            "result": "success",
            "errorCode": "0",
            "orderId": "8a82c561-40b4-4cb3-9bc0-9ac9ffc1d63b"
        }
    },

    # V2 responses
    "https://api.coinone.co.kr/v2/account/user_info": {
        "POST": {
            "result": "success",
            "errorCode": "0",
            "userInfo": {
                "mobileInfo": {
                    "userName": "name",
                    "phoneNumber": "00000000000",
                    "phoneCorp": "0",
                },
                "bankInfo": {
                    "depositor": "name",
                    "accountNumber": "00000000000"
                },
                "emailInfo": {
                    "email": "email@email.email"
                }
            }
        }
    },
    "https://api.coinone.co.kr/v2/account/balance": {
        "POST": {
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
            "btg": {
                "avail": "1.00001234",
                "balance": "1.00001234"
            },
            "krw": {
                "avail": "6901425",
                "balance": "6901430"
            }
        }
    },
    "https://api.coinone.co.kr/v2/order/limit_orders": {
        "POST": {
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
    },
    "https://api.coinone.co.kr/v2/order/complete_orders": {
        "POST": {
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
    },
    "https://api.coinone.co.kr/v2/order/cancel": {
        "POST": {
            "result": "success",
            "errorCode": "0"
        }
    },
    "https://api.coinone.co.kr/v2/order/limit_buy": {
        "POST": {
            "result": "success",
            "errorCode": "0",
            "orderId": "8a82c561-40b4-4cb3-9bc0-9ac9ffc1d63b"
        }

    },
    "https://api.coinone.co.kr/v2/order/limit_sell": {
        "POST": {
            "result": "success",
            "errorCode": "0",
            "orderId": "8a82c561-40b4-4cb3-9bc0-9ac9ffc1d63b"
        }
    }
}


def mock_request(method, url, **kwargs):
    _ = kwargs

    res = MagicMock()
    res.status_code = 200
    res.text = json.dumps(MOCK_RESPONSE_MAP[url][method])

    return res
