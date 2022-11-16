from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import Flask, request, make_response
import json



def get():
    results = run_statment('CALL get_all_uploads_meta()')
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)