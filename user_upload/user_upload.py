from apihelper import check_endpoint_info, fill_optional_data, save_file
from dbhelper import run_statment
from flask import request, make_response
import json
from uuid import uuid4





def post():
    is_valid = check_endpoint_info(request.form, ['title', 'description'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    is_valid = check_endpoint_info(request.files, ['upload_image'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    filename = save_file(request.files['upload_image'])
    if(filename == None):
        return make_response(json.dumps("Sorry, something has gone wrong"), 500)
    
    results = run_statment('CALL post_upload(?,?,?,?)', [request.form['title'], filename, request.form['description'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps('Success'), 200)
    else:
        return make_response(json.dumps(results), 500)
    

def patch():
    is_valid = check_endpoint_info(request.headers, ['token', 'upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_upload_token(?,?)', [request.headers['token'], request.headers['upload_id']])

    results = fill_optional_data(request.json, results[0], ['title','description'])

    results = run_statment('CALL patch_upload(?,?,?,?)', [results['title'], results['description'], request.headers['token'], request.headers['upload_id']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def delete():
    is_valid = check_endpoint_info(request.headers, ['token', 'upload_id']) #maybe upload id
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL delete_upload(?,?)', [request.headers['token'], request.headers['upload_id']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)