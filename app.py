from apihelper import check_endpoint_info, fill_optional_data, save_file
from dbhelper import run_statment
from flask import Flask, request, make_response, send_from_directory
import json
import dbcreds
from uuid import uuid4
import user_login.user_login
import user.user
import user_sensative.user_sensative
import user_upload.user_upload

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
    return user.user.patch()


# user-delete

@app.delete('/api/user')
def delete_user():
    return user.user.delete()


#------------------------- /api/user-sensative -------------------------#
# user-patch sensative ?

@app.get('/api/user-sensative')
def get_user_sensative():
    return user_sensative.user_sensative.get()


@app.patch('/api/user-sensative')
def patch_user_sensative():
    return user_sensative.user_sensative.patch()


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
# get upload  display uploads to everyone even if not logged in

@app.get('/api/user-upload')
def upload_get_data():
    is_valid = check_endpoint_info(request.args, ['upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL ')


# post upload

@app.post('/api/user-upload')
def upload_post():
    return user_upload.user_upload.post()


# patch upload

@app.patch('/api/user-upload')
def upload_patch():
    return user_upload.user_upload.patch()


# delete upload

@app.delete('/api/user-upload')
def upload_delete():
    return user_upload.user_upload.delete()
    
    
#------------------------- /api/user-get-upload-image -------------------------#

# need another enpoint? or add more to it?  or use 2 axios requests? this get and upload get?
@app.get('/api/user-upload-image')
def upload_get():
    is_valid = check_endpoint_info(request.args, ['upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_upload_image(?)', [request.args.get('upload_id')])
    if(type(results) != list):
        return make_response(json.dumps(results, default=str), 500)
    elif(len(results) == 0):
        return make_response(json.dumps("invalid image id"), 400)

    return send_from_directory('images', results[0]['image_ref'])

#------------------------- /api/user-comments -------------------------#
# GET all comments


# POST comment


# PATCH comment


# DELETE comment

#------------------------- /api/upload-tags -------------------------#
# GET tags from upload


# POST a new tag


# DELETE existing tag


#------------------------- /api/favourite -------------------------#
# GET all people you favourited


# POST favoutite someone


# DELETE un-favourite someone


#------------------------- /api/following -------------------------#
# GET all people you're following


# POST follow someone


# DELETE stop following



#------------------------- /api/followed-by -------------------------#
# GET all people you're followed by


if(dbcreds.production_mode == True):
    print("Running in Production Mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5007)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)
