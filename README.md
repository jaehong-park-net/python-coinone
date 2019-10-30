# python-coinone
Coinone bitcoin exchange REST client.

## Prerequisites
+ python3
+ virtualenv
## Install
```
$ git clone https://github.com/jaehong-park-net/python-coinone.git
$ cd python-coinone
$ virtuelenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Test
```
## Just run mocking tests
$ green -vv -r

## Run with real requests (V1 endpoint)
$ COINONE_V1_ACCESS_TOKEN=<your_v1_access_token> green -vv -r

## Run with real requests (V2 endpoint)
$ COINONE_V2_ACCESS_TOKEN=<your_v2_access_token> COINONE_V2_SECRET_KEY=<your_v2_secret_key> green -vv -r

## Run with real requests (V1 & V2 endpoints)
$ COINONE_V1_ACCESS_TOKEN=<your_v1_access_token> COINONE_V2_ACCESS_TOKEN=<your_v2_access_token> COINONE_V2_SECRET_KEY=<your_v2_secret_key> green -vv -r
```

## Example
Simple examples can be found in the test case code.
+ pycoinone/client/test/test_coinone_client_v1.py
+ pycoinone/client/test/test_coinone_client_v2.py