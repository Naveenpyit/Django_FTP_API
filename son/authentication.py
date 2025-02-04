from .encryption import encrypt
from dotenv import load_dotenv
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
load_dotenv()
import os

API_KEY=os.getenv('API_KEY')

class apikeycheck(BaseAuthentication): 
    def authenticate(self,request):
        api_key=request.headers.get('api-key')

        secret_key=''.join(encrypt.encrypt_data(API_KEY))
        print(secret_key)

        if not secret_key:
            raise AuthenticationFailed('Key Must Required!')
        
        if api_key!=secret_key:
            raise AuthenticationFailed("Invalid Key!")
        return None