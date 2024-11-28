import requests
from pprint import pprint
from urllib.parse import urljoin

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter


# Google Authentication 
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client

@api_view(['GET'])
def google_callback_handler(request: Request):
    code = request.query_params['code']
    if code is None:
        raise PermissionError("You are not Authorized!")
    
    res = requests.post('http://127.0.0.1:8000/accounts/google/login/', json={"code": code})
    response = res.json()
    return Response(response)


# GitHub Authentication 
class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://localhost:8000/accounts/github/login/callback/'
    client_class = OAuth2Client

@api_view(['GET', 'POST'])
def github_callback_handler(request: Request):
    print(request.query_params)
    code = request.query_params['code']
    if code is None:
        raise PermissionError("You are not Authorized!")
    
    res = requests.post('http://localhost:8000/accounts/github/login/', json={"code": code})
    response = res.json()
    return Response(response)