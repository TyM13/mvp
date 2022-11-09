from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response
import json
from uuid import uuid4




def get():
    is_valid = check_endpoint_info(request.args, ['user_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL user_get(?)', [request.args.get('user_id')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)



def post():
    is_valid = check_endpoint_info(request.json, ['email', 'name', 'username', 'password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = uuid4().hex
    salt = uuid4().hex
    results = run_statment('CALL user_post(?,?,?,?,?,?)', [request.json.get('email'), request.json.get('name'),
     request.json.get('username'), request.json.get('password'),token, salt])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def delete():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_password = check_endpoint_info(request.json, ['password'])
    if(is_valid != None or is_valid_password != None):
        return make_response(json.dumps(is_valid, is_valid_password, default=str), 400)

    results = run_statment('CALL user_delete(?,?)', [request.json['password'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)