###################################################
#### USER SIDE SCRIPT FOR MAKING CCPA REQUESTS ####
###################################################

import json
import requests


BASE_URL = "http://127.0.0.1:5000/"

user_request = {
    "name": "Anirudh Goyal",
    "email": "anirudhgoyal@utexas.edu",
    "request_type": "know_categories",
}

response = requests.post(url = BASE_URL + "ccpa_request", json = user_request)

print(response.text)
