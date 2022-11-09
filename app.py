from apihelper import check_endpoint_info, fill_optional_data, save_file
from dbhelper import run_statment
from flask import Flask, request, make_response, send_from_directory
import json
import dbcreds
from uuid import uuid4
import user_login.user_login
import user.user

app = Flask(__name__)



#------------------------- /api/user -------------------------#
# user-get

@app.get('/api/user')
def get_user():
    return user.user.get()

# user-post

@app.post('/api/user')
def post_user():
    return user.user.post()



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


# user-patch sensative ?




# user-delete

@app.delete('/api/user')
def delete_user():
    return user.user.delete()




#------------------------- /api/user-login -------------------------#
# user-login

@app.post('/api/user-login')
def login_user():
    return user_login.user_login.post()

# user-logout

@app.delete('/api/user-login')
def logout_user():
    return user_login.user_login.delete()




#------------------------- /api/user-upload -------------------------#

@app.get('/api/user-upload')# need another get?
def upload_get():
    is_valid = check_endpoint_info(request.args, ['upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_upload(?)', [request.args.get('upload_id')])
    if(type(results) != list):
        return make_response(json.dumps(results, default=str), 500)
    elif(len(results) == 0):
        return make_response(json.dumps("invalid image id"), 400)

    return send_from_directory('images', results[0]['image_ref'])

# post upload

@app.post('/api/user-upload')
def upload_post():
    is_valid = check_endpoint_info
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    is_valid = check_endpoint_info(request.files, ['upload_image'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    filename = save_file(request.files['upload_image'])
    if(filename == None):
        return make_response(json.dumps("Sorry, something has gone wrong"), 500)
    
    results = run_statment('CALL post_upload(?,?,?)', [filename, request.form['title'], request.form['description']])
    if(type(results) == list):
        return make_response(json.dumps('Success'), 200)
    else:
        return make_response(json.dumps(results), 500)






if(dbcreds.production_mode == True):
    print("Running in Production Mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5007)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)
