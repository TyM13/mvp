from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response
import json



def patch():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_data = check_endpoint_info(request.json, ['password'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL user_get_sensative(?)', [request.headers.get('token')])
    if(type(results) != list):
        return make_response(json.dumps(results), 400)

    results = run_statment('CALL patch_password(?,?)', [results[0]['password'], request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)