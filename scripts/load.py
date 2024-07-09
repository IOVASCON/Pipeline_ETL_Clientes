# -*- coding: utf-8 -*-
import requests
import json

def load_data(api_endpoint, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
    return response.status_code, response.text
