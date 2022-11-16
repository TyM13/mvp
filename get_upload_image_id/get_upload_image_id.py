from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response, send_from_directory
import json




def get():
# checks the sent data request.args and the expected data upload_id and stores it as the variable is_valid
    is_valid = check_endpoint_info(request.args, ['upload_id'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_upload_image(?)', [request.args['upload_id']])
# if results is not equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't and the length of the results us equal to zero it will return a 400 and the string
    if(type(results) != list):
        return make_response(json.dumps(results, default=str), 500)
    elif(len(results) == 0):
        return make_response(json.dumps("invalid image id"), 400)

# returns the image at results 0 index, uploaded_image
    return send_from_directory('images', results[0]['upload_image'])