from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response
import json



def patch():
# checks the sent data request.headers and the expected data token and stores it as the variable is_valid
    is_valid = check_endpoint_info(request.headers, ['token'])
# checks the sent data request.json and the expected data password, stores it as the variable is_valid_data
    is_valid_data = check_endpoint_info(request.json, ['password'])
# if the variable is_valid or is_valid_data is not equal to none it will send back 400 error and a message (client error)
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

# runs the statment CALL user_get_sensative and sends the token as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL user_get_sensative(?)', [request.headers.get('token')])
# if the type of results is not equal to a list it will display the results and a 400 error message (client error)
    if(type(results) != list):
        return make_response(json.dumps(results), 400)

# runs the statment CALL patch_password and sends the password andtoken as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL patch_password(?,?)', [results[0]['password'], request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)