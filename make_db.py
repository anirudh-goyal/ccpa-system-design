########################################################################
#### SCRIPT FOR MAKING A FAKE REDIS DB WITH REALISTIC PERSONAL INFO ####
########################################################################


import random
from database_helpers import *
import pprint
import redis
import json
import pickle

redis_pre_ccpa = redis.Redis()
redis_post_ccpa = redis.Redis(db=1)
pp = pprint.PrettyPrinter(indent=4)

essential = set(["personal_info", "account_info"]) # must be included in every record

num = 10
filename = "user_side_samples.pkl"
pickle_file = open(filename,'wb')
user_side_samples = []

def add_to_object(user_side_object, data):
    for key, value in data.items():
        user_side_object[key] = value

for i in range(num):
    print((i/num)*100)
    profile = generate_fake_profile()
    pre_ccpa_object = dict()
    post_ccpa_object = dict()
    user_side_object = {"categories": []}
    name = ((profile["personal_info"]["name"]).replace(" ", "_")).lower()
    print("Name = " + name)
    for key in profile:
        include = 1 if (random.randint(0,1) == 1 or key in essential) else 0
        if(include):
            redis_post_ccpa.sadd(name, key)
            redis_pre_ccpa.sadd(name, key)
            name_key = name + ":" + key
            value = {
                "data": profile[key],
                "sensitivity": sensitivity[key],
                "return_to_user": return_to_user[key],
            }
            add_to_object(user_side_object, profile[key])
            user_side_object["categories"].append(key)
            # pp.pprint(value)
            redis_post_ccpa.set(name_key, json.dumps(value))
            redis_pre_ccpa.set(name_key, json.dumps(profile[key]))
    if(random.random() < 0.33):
        user_side_samples.append(user_side_object)

pickle.dump(user_side_samples, pickle_file)
pickle_file.close()




    


