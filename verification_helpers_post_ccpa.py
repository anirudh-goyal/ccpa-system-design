import redis
import json
from datetime import datetime

redis_post_ccpa = redis.Redis(db=1)

def user_exists(user):
    name = user["name"]
    email = user["email"]
    data = redis_post_ccpa.get(name)
    if(data == None):
        return None
    data = json.loads(data)
    if(data["email"]["data"] != email):
        return None
    return data

# returns max sensitivity of data
def get_verification_level(user_data):
    sensitivity = "low"
    for key in user_data:
        if(user_data[key]["sensitivity"] == "high"):
            return("high")
        elif(user_data[key]["sensitivity"] == "medium"):
            sensitivity = "medium"
    return sensitivity

def get_verification_prompts(user):
    user_data = user_exists(user)
    if(user_data == None):
        return None
    else:
        verification_level = get_verification_level(user_data)
        items = sorted(user_data.items(), key = lambda x: x[1]["sensitivity"])
        max_sensitivity = items[-1][1]["sensitivity"]
        verification_prompts = [x[0] for x in items[(-1)*max_sensitivity:]]
        return {"prompts": verification_prompts, "level":verification_level}

def log_verification(user_data, verification_prompts):
    verification_id = int(redis_post_ccpa.get("verification_log_id"))
    redis_post_ccpa.incr("verification_log_id")
    logging_object = {
        "name": user_data["name"],
        "email": user_data["email"],
        "date_received": str(datetime.now()),
        "user_found": 1 if verification_prompts != None else 0, 
        "verification_level": verification_prompts["level"],
        "verification_prompts": verification_prompts["prompts"],
        "verified": 0,
    }
    redis_post_ccpa.set(verification_id, json.dumps(logging_object))
    return verification_id

# u = {"name": "Debra Parker", "email": "kevinreed@gmail.com","password":"io7dzjVe(R"}
# print(get_verification_prompts(u))