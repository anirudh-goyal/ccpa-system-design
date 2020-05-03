#################################################################
#### HELPER FUNCTIONS AND CONSTANTS FOR GENERATING FAKE DATA ####
#################################################################

from faker import Faker
import random

purchasing_history = [
    {
        "product": "iphone",
        "price": 500, 
        "city": "Austin",
    },
    {
        "product": "mac",
        "price": 1000, 
        "city": "San Francisco",
    },
    {
        "product": "cheeseburger",
        "price": 15, 
        "city": "Seattle",
    },
]

def generate_fake_profile():
    fake = Faker()
    profile = fake.profile()
    profile["birthdate"] = str(profile["birthdate"])
    profile["email"] = profile["mail"]
    profile.pop("mail")
    profile.pop("current_location")
    profile.pop("address")
    profile["ssn"] = fake.ssn()
    profile["credit_card"] = fake.credit_card_full()
    profile["outgoing_call_history"] = [fake.phone_number() for i in range(5)]
    random.shuffle(purchasing_history)
    profile["purchasing_history"] = purchasing_history
    profile["password"] = fake.password()
    profile["security_question1"] = fake.name()
    profile["security_question2"] = fake.location_on_land()[2]
    return profile

low = "low"
medium = "medium"
high = "high"

fake = Faker()

sensitivity = {
    "job": 1,
    "company": 1,
    "ssn": 3, 
    "residence": 2,
    "blood_group": 3, 
    "website": 1,
    "username": 1, 
    "name": 1, 
    "sex": 1, 
    "email": 1, 
    "birthdate": 2,
    "driving_license": 3, 
    "credit_card": 3, 
    "purchasing_history": 2, 
    "outgoing_call_history": 2,
    "password": 2,
    "security_question1": 3, 
    "security_question2": 3,
}

return_to_user = {
    "job": 1,
    "company": 1,
    "ssn": 0, 
    "residence": 1,
    "blood_group": 0, 
    "website": 1,
    "username": 1, 
    "name": 1, 
    "sex": 1, 
    "email": 1, 
    "birthdate": 1,
    "driving_license": 0, 
    "credit_card": 1, 
    "purchasing_history": 1, 
    "outgoing_call_history": 1,
    "password": 0,
    "security_question1": 0, 
    "security_question2": 0,
}