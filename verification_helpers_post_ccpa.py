import redis
import json

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
        return verification_prompts

u = {"name": "Debra Parker", "email": "kevinreed@gmail.com","password":"io7dzjVe(R"}
print(get_verification_prompts(u))