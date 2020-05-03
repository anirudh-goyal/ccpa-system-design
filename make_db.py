########################################################################
#### SCRIPT FOR MAKING A FAKE REDIS DB WITH REALISTIC PERSONAL INFO ####
########################################################################


import random
from database_helpers import *
import pprint
import redis
import json

redis_pre_ccpa = redis.Redis()
redis_post_ccpa = redis.Redis(db=1)
pp = pprint.PrettyPrinter(indent=4)

essential = set(["name", "email", "password"]) # must be included in every record

profile = generate_fake_profile()
pre_ccpa_object = dict()
post_ccpa_object = dict()

for key in profile:
    include = 1 if (random.randint(0,1) == 1 or key in essential) else 0
    if(include):
        pre_ccpa_object[key] = profile[key]
        post_ccpa_object[key] = {
            "data": profile[key], 
            "sensitivity": sensitivity[key], 
            "return_to_user": return_to_user[key]
        }
# pp.pprint(pre_ccpa_object)
# pp.pprint(post_ccpa_object)
print(post_ccpa_object["name"]["data"])
redis_post_ccpa.set(post_ccpa_object["name"]["data"], json.dumps(post_ccpa_object))
redis_pre_ccpa.set(pre_ccpa_object["name"], json.dumps(pre_ccpa_object))
# x = r.get("mykey").decode("utf-8")






    


