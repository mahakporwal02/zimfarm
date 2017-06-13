from calendar import timegm
from datetime import datetime

import jwt

secret = 'secret'


def jwt_encode(payload) -> str:
    return jwt.encode(payload, secret, algorithm='HS256').decode()


def jwt_decode(encoded: str):
    return jwt.decode(encoded, secret, algorithms=['HS256'])


def utc_timestamp():
    return timegm(datetime.utcnow().utctimetuple())