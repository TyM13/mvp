from apihelper import check_endpoint_info, fill_optional_data
from dbhelper import run_statment
from flask import request, make_response
import json


def get():
    is_valid = check_endpoint_info(request.args, ['token'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

# runs the statment CALL user_get_sensative and sends the token as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL user_get_sensative(?)', [request.args.get('token')])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)



def patch():
# checks the sent data request.headers and the expected data token stores it as the variable is_valid
    is_valid = check_endpoint_info(request.headers, ['token'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

# runs the statment CALL user_get_sensative and sends the token as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL user_get_sensative(?)', [request.headers.get('token')])
# if the type of results is not equal to a list it will display the results and a 400 error message (client error)
    if(type(results) != list):
        return make_response(json.dumps(results), 400)

# it will request info from results at the index 0 and fill in all the information it as the same info
    results = fill_optional_data(request.json, results[0], ['email','phone_number',
    'date_of_birth'])

# runs the statment CALL user_patch_sensative and sends the email, phone_number, DoB and token as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL user_patch_sensative(?,?,?,?)', [results['email'], results['phone_number'],
    results['date_of_birth'], request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)