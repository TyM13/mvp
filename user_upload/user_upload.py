from apihelper import check_endpoint_info, fill_optional_data, save_file
from dbhelper import run_statment
from flask import request, make_response
import json





def post():
# checks the sent data request.form and the expected data title, description stores it as the variable is_valid
    is_valid = check_endpoint_info(request.form, ['title', 'description'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    is_valid = check_endpoint_info(request.files, ['upload_image'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    filename = save_file(request.files['upload_image'])
    if(filename == None):
        return make_response(json.dumps("Sorry, something has gone wrong"), 500)

# runs the statment CALL post_upload and sends the title, description and token as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL post_upload(?,?,?,?)', [request.form['title'], filename, request.form['description'], request.headers['token']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps('Success'), 200)
    else:
        return make_response(json.dumps(results), 500)
    

def patch():
# checks the sent data request.headers and the expected data upload_id, token stores it as the variable is_valid
    is_valid = check_endpoint_info(request.headers, ['token', 'upload_id'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

# runs the statment CALL get_upload_token and sends the token and upload_id as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL get_upload_token(?,?)', [request.headers['token'], request.headers['upload_id']])
# if the type of results is not equal to a list it will display the results and a 400 error message (client error)
    if(type(results) != list):
        return make_response(json.dumps(results), 400)

# it will request info from results at the index 0 and fill in all the information it as the same info
    results = fill_optional_data(request.json, results[0], ['title','description'])

# runs the statment CALL patch_upload and sends the title, description and token and upload_id as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL patch_upload(?,?,?,?)', [results['title'], results['description'], request.headers['token'], request.headers['upload_id']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def delete():
# checks the sent data request.headers and the expected data upload_id, token stores it as the variable is_valid
    is_valid = check_endpoint_info(request.headers, ['token', 'upload_id'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

# runs the statment CALL delete_upload and sends the token and upload_id as an arguement and stores the select statmentment from the procedure as results
    results = run_statment('CALL delete_upload(?,?)', [request.headers['token'], request.headers['upload_id']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)