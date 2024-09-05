from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import requests
from pprint import pprint

@api_view(['GET'])
def google_callback(request: Request):
    code = request.query_params['code']
    response = requests.post('http://127.0.0.1:8000/dj-rest-auth/google/', json={"code": code})
    json_response = response.json()

    print("---------------------------")
    pprint(json_response)
    print("---------------------------")
    return Response('Hello!')