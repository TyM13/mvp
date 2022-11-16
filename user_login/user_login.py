from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response
import json
from uuid import uuid4



def post():
    is_valid = check_endpoint_info(request.json, ['email','password'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = uuid4().hex 
# runs the statment CALL user_login and sends the email, password and token (generated token) as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL user_login(?,?,?)', [request.json['email'], request.json['password'], token])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if you put in the wrong info it will give you a 400 message (user client error)
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    elif(type(results) == list):
        return make_response(json.dumps("Bad login attempt"), 400)
    else:
        return make_response(json.dumps("Sorry there has been an error"), 500) 




def delete():
# checks the sent data request.headers and the expected data token stores it as the variable is_valid
    is_valid = check_endpoint_info(request.headers, ['token'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

# runs the statment CALL user_logout and sends the token as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL user_logout(?)', [request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)