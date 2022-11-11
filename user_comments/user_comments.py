from apihelper import check_endpoint_info, fill_optional_data, save_file
from dbhelper import run_statment
from flask import request, make_response
import json
from uuid import uuid4




def get():
    is_valid = check_endpoint_info(request.args, ['upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_comments(?)', [request.args.get('upload_id')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def post():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_data = check_endpoint_info(request.json, ['content' ,'upload_id'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL post_comment(?,?,?)', [request.json['content'], request.json['upload_id'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def patch():
    is_valid = check_endpoint_info(request.headers, ['upload_id', 'token'])
    is_valid_data = check_endpoint_info(request.json, ['content'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL patch_comments(?,?,?)', [request.json['content'], request.headers['upload_id'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


def delete():
    is_valid = check_endpoint_info(request.headers, ['upload_id', 'token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL delete_comments(?,?)', [request.headers['upload_id'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)