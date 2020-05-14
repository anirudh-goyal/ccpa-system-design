#################################################################
#### HELPER FUNCTIONS AND CONSTANTS FOR GENERATING FAKE DATA ####
#################################################################

from faker import Faker
import random
import pprint


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

diseases = ["Anemia", "Appendicitis", "Arthritis", "Asthma", "Bacteria"]

def remove_keys(dictionary, keys):
    for k in keys:
        dictionary.pop(k)

pp = pprint.PrettyPrinter(indent=4)

def generate_fake_profile():
    fake = Faker()
    profile = fake.profile()
    random.shuffle(purchasing_history)
    new_profile = {}
    new_profile["personal_info"] = {
        "name": profile["name"].replace(":",""),
        "birthdate": str(profile["birthdate"]),
        "email": profile["mail"],
        "phone": fake.phone_number(),
        "residence": profile["residence"],
        "sex": profile["sex"]
    }
    new_profile["account_info"] = {
        "username": profile["username"],
        "password": fake.password()
    }
    new_profile["security_questions"] = {
        "security_question1": fake.name(), 
        "security_question2": fake.location_on_land()[2],
    }
    new_profile["account_history"] = {
        "purchasing_history": purchasing_history,
        "outgoing_call_history": [fake.phone_number() for i in range(5)]
    }
    new_profile["health_info"] = {
        "past_diseases": random.sample(diseases, 3),
        "blood_group": profile["blood_group"]
    }
    new_profile["financial_info"] = {
        "credit_card": fake.credit_card_full(),
        "bank_account": random.randint(5425425431, 5425425431 + 500000)
    }
    new_profile["government_ids"] = {
        "ssn": fake.ssn(),
        "driving_license": "DL" + fake.ssn()
    }
    new_profile["employment"] = {
        "employer": profile["company"],
        "job_title": profile["job"],
        "website": profile["website"][0]
    }
    return new_profile

low = "low"
medium = "medium"
high = "high"

fake = Faker()

sensitivity = {
    "personal_info": 1,
    "account_info": 2,
    "security_questions": 2,
    "account_history": 2, 
    "health_info": 3,
    "financial_info": 3,
    "government_ids": 3, 
    "employment": 1,
}

return_to_user = {
    "personal_info": 1,
    "account_info": 1,
    "security_questions": 0,
    "account_history": 1, 
    "health_info": 0,
    "financial_info": 1,
    "government_ids": 0, 
    "employment": 1,
}

# pp.pprint(generate_fake_profile())