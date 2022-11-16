from apihelper import check_endpoint_info
from flask import request, make_response, send_from_directory
import json



def get():
# checks the sent data request.args and the expected data file_name and stores it as the variable is_valid
    is_valid = check_endpoint_info(request.args, ['file_name'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)


    return send_from_directory('images', request.args['file_name'])