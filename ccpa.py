###################################################
#### USER SIDE SCRIPT FOR MAKING CCPA REQUESTS ####
###################################################

import json
import requests
import pickle


BASE_URL = "http://127.0.0.1:5000/"

# user_request = {
#     "name": "Anirudh Goyal",
#     "email": "anirudhgoyal@utexas.edu",
#     "request_type": "know_categories",
# }

filename = "user_side_samples.pkl"
pickle_file = open(filename, 'rb')
user_side_samples = pickle.load(pickle_file)

def get_verification_data(user, prompts):
    data = {}
    for p in prompts:
        data[p] = user[p]
    return data

def make_request(user):
    requested_categories = random.sample(user["categories"], 3)
    name = user["name"]
    email = user["email"]
    request_type = "know"
    password = "xyz"
    payload = {
        "name": name, 
        "email": email,
        "password": password,
        "request_type": request_type,
        "categories": requested_categories
    }
    response = json.loads((requests.post(url = BASE_URL + "ccpa_request", json = u)).text)
    return response

def do_ccpa_request(user):
    initial_response = make_request(user)
    verified = send_verification_data(user, initial_response)

def send_verification_data(user, initial_response):
    verification_prompts = initial_response["verification_prompts"]
    verification_id = initial_response["verification_id"]
    verification_data = get_verification_data(user, verification_prompts)
    payload = {
        "verification_id": verification_id,
        "name": user["name"],
        "email": user["email"],
        "user_verification_data": verification_data,
    }
    verified_response = json.loads((requests.post(url = BASE_URL + "verify_user", json = payload)).text)
    return verified_response


# initial_response = json.loads((requests.post(url = BASE_URL + "ccpa_request", json = u)).text)

# verification_prompts = initial_response["verification_prompts"]
# verification_id = initial_response["verification_id"]

# payload = {
#     "verification_id": verification_id,
#     "name": user["name"],
#     "email": user["email"],
#     "user_verification_data": get_verification_data(user, verification_prompts),
# }

# verified_response = json.loads((requests.post(url = BASE_URL + "verify_user", json = payload)).text)

# print(verified_response)
