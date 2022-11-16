from apihelper import check_endpoint_info
from flask import request, make_response, send_from_directory
import json



def get():
    is_valid = check_endpoint_info(request.args, ['file_name'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)


    return send_from_directory('images', request.args['file_name'])