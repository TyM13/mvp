from apihelper import check_endpoint_info, fill_optional_data
from dbhelper import run_statment
from flask import request, make_response
import json
from uuid import uuid4




def get():
# checks the sent data request.args and the expected data user_id and stores it as the variable is_valid
    is_valid = check_endpoint_info(request.args, ['user_id'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

# runs the statment CALL user_get and sends the user_id as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL user_get(?)', [request.args.get('user_id')])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)



def post():
# checks the sent data request.json and the expected data email,name,username,password and stores it as the variable is_valid
    is_valid = check_endpoint_info(request.json, ['email', 'name', 'username', 'password'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

# generates a random unique id and sets it as the variable token and salt
    token = uuid4().hex
    salt = uuid4().hex
# runs the statment CALL user_post and sends all the request.json as well as token and salt as arguements
#  and stores the select statmentment from the procedure as results
    results = run_statment('CALL user_post(?,?,?,?,?,?)', [request.json.get('email'), request.json.get('name'),
     request.json.get('username'), request.json.get('password'),token, salt])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def patch():
# checks the sent data request.headers and the expected data token and stores it as the variable is_valid
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
    results = fill_optional_data(request.json, results[0], ['name','profile_photo','username',
    'bio','links'])

# runs the statment CALL user_patch and sends name, profile_photo, username, bio, links, token
# as arguements and stores the select statmentment from the procedure as results 
    results = run_statment('CALL user_patch(?,?,?,?,?,?)', [results['name'], results['profile_photo'], results['username'],
     results['bio'], results['links'], request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)




def delete():
# checks the sent data request.headers and the expected data token, stores it as the variable is_valid
    is_valid = check_endpoint_info(request.headers, ['token'])
# checks the sent data request.json and the expected data password, stores it as the variable is_valid_data
    is_valid_password = check_endpoint_info(request.json, ['password'])
# if the variable is_valid or is_valid_data is not equal to none it will send back 400 error and a message (client error)
    if(is_valid != None or is_valid_password != None):
        return make_response(json.dumps(is_valid, is_valid_password, default=str), 400)

# runs the statment CALL user_delete and sends the password and token as an arguement and stores the select statmentment from the procedure as results 
    results = run_statment('CALL user_delete(?,?)', [request.json['password'], request.headers['token']])
    if(type(results) == list):
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)