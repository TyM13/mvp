from apihelper import check_endpoint_info, fill_optional_data
from dbhelper import run_statment
from flask import request, make_response
import json
from uuid import uuid4


def patch():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_data = check_endpoint_info(request.json, ['password'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL user_get_sensative(?)', [request.headers.get('token')])
    if(type(results) != list):
        return make_response(json.dumps(results), 400)

    results = run_statment('CALL patch_password(?,?)', [results[0]['password'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)