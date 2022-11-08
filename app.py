from apihelper import check_endpoint_info, fill_optional_data
from dbhelper import run_statment
from flask import Flask, request, make_response
import json
import dbcreds
from uuid import uuid4

app = Flask(__name__)



#------------------------- /api/user -------------------------#
# user-get

@app.get('/api/user')
def get_user():
    is_valid = check_endpoint_info(request.args, ['user_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL user_get(?)', [request.args.get('user_id')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


# user-post

@app.post('/api/user')
def post_user():
    is_valid = check_endpoint_info(request.json, ['email', 'name', 'username', 'password'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    token = uuid4().hex
    salt = uuid4().hex
    results = run_statment('CALL user_post(?,?,?,?,?,?)', [request.json.get('email'), request.json.get('name'),
     request.json.get('username'), request.json.get('password'),token, salt])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


# user-patch

@app.patch('/api/user')
def patch_user():
    is_valid = check_endpoint_info(request.headers, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL user_get_sensative(?)', request.headers.get('token'))
    if(type(results) != list):
        return make_response(json.dumps(results), 400)

    results = fill_optional_data(request.json, results[0], ['name','profile_photo','username',
    'bio','links'])

    results = run_statment('CALL user_patch(?,?,?,?,?)', [results['name'], results['profile_photo'], results['username'],
     results['bio'], results['links'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


# user-patch sensative




# user-delete

@app.delete('/api/user')
def delete_user():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_password = check_endpoint_info(request.json, ['password'])
    if(is_valid != None or is_valid_password != None):
        return make_response(json.dumps(is_valid, is_valid_password, default=str), 400)

    results = run_statment('CALL user_delete(?,?)', [request.json['password'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)




#------------------------- /api/user-login -------------------------#
# user-login







if(dbcreds.production_mode == True):
    print("Running in Production Mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5007)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)
