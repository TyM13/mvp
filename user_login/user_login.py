from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response
import json
from uuid import uuid4



def post():
    is_valid = check_endpoint_info(request.json, ['email','password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = uuid4().hex 
    results = run_statment('CALL user_login(?,?,?)', [request.json['email'], request.json['password'], token])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    elif(type(results) == list):
        return make_response(json.dumps("Bad login attempt"), 400)
    else:
        return make_response(json.dumps("Sorry there has been an error"), 500) 




def delete():
    is_valid = check_endpoint_info(request.headers, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL user_logout(?)', [request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)