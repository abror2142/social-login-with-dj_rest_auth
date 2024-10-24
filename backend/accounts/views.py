import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client


@api_view(['GET'])
def google_callback_handler(request: Request):
    code = request.query_params['code']
    response = requests.post('http://127.0.0.1:8000/accounts/google/login/', json={"code": code})
    json_response = response.json()
    print(json_response)
    return Response('Hello!')

