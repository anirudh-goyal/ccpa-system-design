####################################################
#### COMPANY SIDE SERVER HANDLING USER REQUESTS ####
####################################################


from flask import Flask 
from flask import request
from flask import jsonify
import json
from verification_helpers_post_ccpa import *
app = Flask(__name__)

# submit name, email, and which type of request
@app.route('/ccpa_request', methods=['POST'])
def ccpa_request():
    request_data = json.loads(request.data)
    verification_prompts = get_verification_prompts(request_data)
    verification_log_id = log_verification(request_data, verification_prompts)
    response = {
        "name": request_data["name"],
        "request_id": verification_log_id,
        "user_found": 1 if verification_prompts != None else 0,
        "login_authorized": 1,
        "verification_prompts": verification_prompts["prompts"],
    }
    print(response)
    return jsonify(response)

@app.route('/send_identification', methods=['POST'])
def verify_identification():
    # request_data = json.loads(request.data)
    # result = verify_user(request_data) #send to govt agency also
    # result
    # {
    #     request_id:
    #     verified: yes or no 
    #     additional_info_required: {}
    # }
    return "OK"

if __name__ == "__main__":
    app.run()