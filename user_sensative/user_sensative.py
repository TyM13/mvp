from apihelper import check_endpoint_info, fill_optional_data
from dbhelper import run_statment
from flask import request, make_response
import json
from uuid import uuid4


def get():
    is_valid = check_endpoint_info(request.args, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL user_get_sensative(?)', [request.args.get('token')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)



def patch():
    is_valid = check_endpoint_info(request.headers, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL user_get_sensative(?)', [request.headers.get('token')])
    if(type(results) != list):
        return make_response(json.dumps(results), 400)

    results = fill_optional_data(request.json, results[0], ['email','phone_number',
    'date_of_birth'])

    results = run_statment('CALL user_patch_sensative(?,?,?,?)', [results['email'], results['phone_number'],
    results['date_of_birth'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)