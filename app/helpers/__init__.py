from flask import jsonify, make_response
import jwt
import datatime import datetime, timedelta

from app.config import BaseConfig

@staticmethod
def encode_auth_token(self, user_email="iproudyou@gmail.com", min_expires=15):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=min_expires, seconds=0),
            'lat': datetime.utcnow(),
            'sub': user_email
        }
        token = jwt.encode(
            payload,
            BaseConfig.API_SECRET_KEY,
            algorithm='HS256'
        )
        return token
    except Exception as e:
        return e
        
@staticmethod
def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, BaseConfig.API_SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired.'
    except jwt.InvalidTokenError:
        return 'Invalid Token.'
    
@staticmethod
def is_unauthorized():
    """Ensure a user is authorized to access a certain resource"""
    response_payload = dict(
        message = 'Invalid token to use this resource!'
    )
    return make_response(jsonify(response_payload), 401)
