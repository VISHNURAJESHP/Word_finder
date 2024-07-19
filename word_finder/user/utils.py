import jwt
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from django.conf import settings

def authenticate_user(token):
    if not token:
        raise AuthenticationFailed('User is not found')
    
    try:
        secret_key = settings.HASH_KEY
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user_id = payload['id']
        user = User.objects.get(id=user_id)
        return user
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("The Token is expired")
    except jwt.InvalidTokenError:
        raise AuthenticationFailed("Invalid Token")
    except User.DoesNotExist:
        raise AuthenticationFailed("User not found")