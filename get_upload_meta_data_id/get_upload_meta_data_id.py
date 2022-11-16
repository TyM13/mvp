from apihelper import check_endpoint_info, fill_optional_data, save_file
from dbhelper import run_statment
from flask import Flask, request, make_response, send_from_directory
import json
import dbcreds
from uuid import uuid4



def get():
    is_valid = check_endpoint_info(request.args, ['upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_meta_data(?)', [request.args['upload_id']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)