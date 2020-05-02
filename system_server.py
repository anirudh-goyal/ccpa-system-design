####################################################
#### COMPANY SIDE SERVER HANDLING USER REQUESTS ####
####################################################


from flask import Flask 
from flask import request
import json
app = Flask(__name__)

# submit name, email, and which type of request
@app.route('/ccpa_request', methods=['POST'])
def ccpa_request():
    request_data = json.loads(request.data)
    print(request_data)
    return "OK"
    # verification_method = find_verification_method(request_data)
    # verification_method 
    # {
    #     request_id: # NONE if user not found
    #     stringency_level:
    #     data_point1:
    #     data_point2:
    #     data_point3:
    # }
    # return(jsonify(verification_method))

@app.route('/send_identification', methods=['POST'])
def verify_identification():
    request_data = json.loads(request.data)
    result = verify_user(request_data) #send to govt agency also
    # result
    # {
    #     request_id:
    #     verified: yes or no 
    #     additional_info_required: {}
    # }

if __name__ == "__main__":
    app.run()