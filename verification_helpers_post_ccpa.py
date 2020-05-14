import redis
import json
from datetime import datetime

redis_post_ccpa = redis.Redis(db=1)

def user_exists(user):
    name = user["name"]
    email = user["email"]
    name_exists = redis_post_ccpa.exists(name)
    if(not name_exists):
        return False
    personal_info = redis_post_ccpa.get(name + ":" + "personal_info")
    db_email = json.loads(personal_info)["data"]["email"]
    if(db_email != email):
        return False
    return True

# returns max sensitivity of data
def get_verification_level(user_data):
    sensitivity = "low"

    for key in user_data:
        if(user_data[key]["sensitivity"] == "high"):
            return("high")
        elif(user_data[key]["sensitivity"] == "medium"):
            sensitivity = "medium"
    return sensitivity

def get_prompts(user):
    categories = user["categories"]
    name = user["name"]
    all_categories = [x.decode("utf-8") for x in redis_post_ccpa.smembers(name)]
    request_sensitivity = 0
    data = []
    for c in all_categories:
        category_data = json.loads(redis_post_ccpa.get(name + ":" + c))
        category_sensitivity = category_data["sensitivity"]
        if(c in categories):
            request_sensitivity = max(request_sensitivity, category_sensitivity)
        for data_point in category_data["data"]:
            data.append((data_point, category_sensitivity))
    print("Request sensitivity = " + str(request_sensitivity))
    data = sorted(data, key=lambda x: x[1])
    prompts = [x[0] for x in data[(-1)*request_sensitivity:]]
    print(data)
    print(prompts)
    return request_sensitivity, prompts

def get_verification_prompts(user):
    if(not user_exists(user)):
        log_object = log_verification(user, 0, 0, None)
        return log_object
    else:
        request_sensitivity, prompts = get_prompts(user)
        log_object = log_verification(user, 1, request_sensitivity, prompts)
        return log_object

def log_verification(user, user_found, request_sensitivity, verification_prompts):
    verification_id = int(redis_post_ccpa.get("verification_log_id"))
    redis_post_ccpa.incr("verification_log_id")
    logging_object = {
        "verification_id": verification_id,
        "name": user["name"],
        "email": user["email"],
        "date_received": str(datetime.now()),
        "user_found": user_found, 
        "verification_level": request_sensitivity,
        "verification_prompts": verification_prompts,
        "verified": 0,
    }
    redis_post_ccpa.set(verification_id, json.dumps(logging_object))
    return logging_object

# u = {"name": "Debra Parker", "email": "kevinreed@gmail.com","password":"io7dzjVe(R"}
# print(get_verification_prompts(u))