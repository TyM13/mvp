from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response
import json




def get():
    is_valid = check_endpoint_info(request.args, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)
    
    results = run_statment('CALL get_following(?)', [request.args['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def post():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_data = check_endpoint_info(request.json, ['following_user_id'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL post_following(?,?)', [request.json['following_user_id'], request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def delete():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_data = check_endpoint_info(request.json, ['following_user_id'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL delete_following(?,?)', [request.json['following_user_id'] ,request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)