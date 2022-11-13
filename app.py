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
import user_comments.user_comments
import user_favourites.user_favourites
import upload_tags.upload_tags

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


#------------------------- /api/change-password -------------------------#
# change password

@app.patch('/api/patch-password')
def password_patch():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_data = check_endpoint_info(request.json, ['password'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL user_get_sensative(?)', [request.headers.get('token')])
    if(type(results) != list):
        return make_response(json.dumps(results), 400)

    results = run_statment('CALL patch_password(?,?)', [results[0]['password'], request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)

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
# get upload  display uploads to everyone even if not logged in no required data limit amount from newest

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
    
    
#------------------------- /api/get-upload-image -------------------------#

# need another enpoint? or add more to it?  or use 2 axios requests? this get and upload get?
@app.get('/api/user-upload-image')
def upload_get():
    is_valid = check_endpoint_info(request.args, ['upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_upload_image(?)', [request.args['upload_id']])
    if(type(results) != list):
        return make_response(json.dumps(results, default=str), 500)
    elif(len(results) == 0):
        return make_response(json.dumps("invalid image id"), 400)

    return send_from_directory('images', results[0]['upload_image'])

#------------------------- /api/get-meta-data -------------------------#


@app.get('/api/upload-meta-data')
def meta_data_get():
    is_valid = check_endpoint_info(request.args, ['upload_id'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statment('CALL get_meta_data(?)', [request.args['upload_id']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)

#------------------------- /api/user-comments -------------------------#
# GET all comments

@app.get('/api/user-comments')
def comments_get():
    return user_comments.user_comments.get()


# POST comment

@app.post('/api/user-comments')
def comments_post():
    return user_comments.user_comments.post()


# PATCH comment


@app.patch('/api/user-comments')
def comments_patch():
    return user_comments.user_comments.patch()


# DELETE comment

@app.delete('/api/user-comments')
def comments_delete():
    return user_comments.user_comments.delete()

#------------------------- /api/upload-tags -------------------------#
# GET tags from upload

@app.get('/api/upload-tags')
def tags_get():
    return upload_tags.upload_tags.get()

# POST a new tag

@app.post('/api/upload-tags')
def tags_post():
    return upload_tags.upload_tags.post()


# DELETE existing tag

@app.delete('/api/upload-tags')
def tags_delete():
    return upload_tags.upload_tags.delete()

#------------------------- /api/user-favourite -------------------------#
# GET all people you favourited

@app.get('/api/user-favourite')
def favourite_get():
    return user_favourites.user_favourites.get()


# POST favoutite someone

@app.post('/api/user-favourite')
def favourite_post():
    return user_favourites.user_favourites.post()


# DELETE un-favourite someone

@app.delete('/api/user-favourite')
def favourite_delete():
    return user_favourites.user_favourites.delete()

#------------------------- /api/following -------------------------#
# GET all people you're following

@app.get('/api/following')
def following_get():
    is_valid = check_endpoint_info(request.args, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)
    
    results = run_statment('CALL get_following(?)', [request.args['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)

# POST follow someone  MIGHT BE WRONG NEED TO CHECK PROCEDURE
# @app.post('/api/following')
# def following_post():
#     is_valid = check_endpoint_info(request.headers, ['token'])
#     is_valid_data = check_endpoint_info(request.json, ['following_user_id', 'followed_by_user_id'])
#     if(is_valid != None or is_valid_data != None):
#         return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

#     results = run_statment('CALL post_following(?,?,?)', [request.json['following_user_id'],request.json['followed_by_user_id'], request.headers['token']])
#     if(type(results) == list):
#         return make_response(json.dumps(results, default=str), 200)
#     else:
#         return make_response(json.dumps(results, default=str), 500)


# DELETE stop following

@app.delete('/api/following')
def following_delete():
    is_valid = check_endpoint_info(request.headers, ['token'])
    is_valid_data = check_endpoint_info(request.json, ['following_user_id'])
    if(is_valid != None or is_valid_data != None):
        return make_response(json.dumps(is_valid, is_valid_data, default=str), 400)

    results = run_statment('CALL delete_following(?,?)', [request.json['following_user_id'] ,request.headers['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


#------------------------- /api/followed-by -------------------------#
# GET all people you're followed by
@app.get('/api/followed-by')
def followed_by_get():
    is_valid = check_endpoint_info(request.args, ['token'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)
    
    results = run_statment('CALL get_followed_by(?)', [request.args['token']])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


#------------------------- /api/get-all-images -------------------------#

@app.get('/api/get-all-images')
def upload_get_all_images():
    is_valid = check_endpoint_info(request.args, ['file_name'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)


    return send_from_directory('images', request.args['file_name'])

#------------------------- /api/get-all-uploads-meta -------------------------#

@app.get('/api/get-all-uploads-meta')
def upload_get_all_uploads_meta():
    results = run_statment('CALL get_all_uploads_meta()')
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 500)


if(dbcreds.production_mode == True):
    print("Running in Production Mode")
    import bjoern # type: ignore
    bjoern.run(app, "0.0.0.0", 5007)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    app.run(debug=True)





#  call post_favourite(6,'token');

#  call get_favourite('919f568243a549ffbe14f53bc3e9af5a');

#  call delete_favourite(6,'token');

#  call post_tag('TAG!', 6,'919f568243a549ffbe14f53bc3e9af5a');

#  call get_tags(7);

#  call delete_tags(5,'token');

#  call post_following(1,'919f568243a549ffbe14f53bc3e9af5a');

#  call get_following('token');

#  call delete_following(1,'919f568243a549ffbe14f53bc3e9af5a');

#  call get_followed_by('token');
 
# call test(1,'919f568243a549ffbe14f53bc3e9af5a');

# call patch_password('passwords','token');

# call get_upload_image(6);

# call get_all_uploads();

# call get_all_images();