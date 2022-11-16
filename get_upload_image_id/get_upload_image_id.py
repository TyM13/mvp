from apihelper import check_endpoint_info, fill_optional_data
from dbhelper import run_statment
from flask import request, make_response, send_from_directory
import json
from uuid import uuid4



def get():
    is_valid = check_endpoint_info(request.args, ['upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_upload_image(?)', [request.args['upload_id']])
    if(type(results) != list):
        return make_response(json.dumps(results, default=str), 500)
    elif(len(results) == 0):
        return make_response(json.dumps("invalid image id"), 400)

    return send_from_directory('images', results[0]['upload_image'])