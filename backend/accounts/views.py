import requests
from pprint import pprint
from urllib.parse import urljoin

import requests
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter



class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client


@api_view(['GET'])
def google_callback_handler(request: Request):
    code = request.query_params['code']
    if code is None:
        print("There is no Code!")
        raise PermissionError("You are not Authorized!")
    
    res = requests.post('http://127.0.0.1:8000/accounts/google/login/', json={"code": code})
    response = res.json()
    print('Refresh', response)
    return Response(response)