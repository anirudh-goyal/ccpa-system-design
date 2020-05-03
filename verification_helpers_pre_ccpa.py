import redis
import json

redis_pre_ccpa = redis.Redis()

def user_exists(user):
    name = user["name"]
    email = user["email"]
    data = redis_pre_ccpa.get(name)
    if(data == None):
        return None
    data = json.loads(data)
    if(data["email"] != email):
        return None
    return data
    
def get_user_data_from_db(user):
    user_data = user_exists(user)
    return user_data

def delete_user_data_from_db(user):
    if(user_exists(user) == None):
        return False
    else:
        name = user["name"]
        redis_pre_ccpa.delete(name)
        return True

def auth_user(user):
    user_data = user_exists(user)
    if(user_data == None):
        return False
    else:
        email = user["email"]
        password = user["password"]
        return (email == user_data["email"] and password == user_data["password"])

def get_user_data_categories(user):
    user_data = user_exists(user)
    if(user_data == None):
        return None
    else:
        return list(user_data.keys())




# print(get_user_data_from_db({"name": "Brenda Kim", "email": "vsmith@hotmail.com","password":"+eWm3Za_z8"}))
# print(get_user_data_categories({"name": "Brenda Kim", "email": "vsmith@hotmail.com","password":"+eWm3Za_z8"}))
# print(auth_user({"name": "Brenda Kim", "email": "vsmith@hotmail.com","password":"+eWm3Za_z8"}))
# print(delete_user_data_from_db({"name": "Brenda Kim", "email": "vsmith@hotmail.com","password":"+eWm3Za_z8"}))


