from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response
import json





def get():
# checks the sent data request.args and the expected data token stores it as the variable is_valid
    is_valid = check_endpoint_info(request.args, ['token'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_favourite(?)', [request.args['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def post():
# checks the sent data request.headers and the expected data token stores it as the variable is_valid
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_data = check_endpoint_info(request.json, ['upload_id'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL post_favourite(?,?)', [request.json['upload_id'],request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)



def delete():
# checks the sent data request.headers and the expected data token stores it as the variable is_valid
    is_valid = check_endpoint_info(request.headers, ['token'])
# checks the sent data request.json and the expected data upload_id, stores it as the variable is_valid_data
    is_valid_data = check_endpoint_info(request.json, ['upload_id'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL delete_favourite(?,?)', [request.json['upload_id'],request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)