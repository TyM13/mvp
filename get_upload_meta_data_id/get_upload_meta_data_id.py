from apihelper import check_endpoint_info
from dbhelper import run_statment
from flask import request, make_response
import json




def get():
# checks the sent data request.args and the expected data upload_id and stores it as the variable is_valid
    is_valid = check_endpoint_info(request.args, ['upload_id'])
# if the variable is_valid is not none it will send back 400 error and a message (client error)
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)


# runs the statment CALL get_meta_data and sends the upload_id as an arguement and stores the select statmentment from the procedure as results 
    results = run_statment('CALL get_meta_data(?)', [request.args['upload_id']])
# if results is equal to a list it will display a 200 message (success), and print the results of the procedure as json 
# if it isn't it will display a 500 message (server error)
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)