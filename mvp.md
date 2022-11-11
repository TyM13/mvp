# MVP


# Endpoints

## `User`

**URL: http://127.0.0.1:5000/api/user**  
Supported HTTP Methods: **GET, POST, PATCH, DELETE**

### `GET`

Returns information about a single user, will error if the client_id does not exist.

**Required Params:**

```
{
    user_id: (number)
}
```

**Data Returned**

```
{   
    id: (number), 
    name: (string),
    username: (string),
    bio: (string),
    links: (string),
    profile_photo: (string),
    created_at: (string)
}
```

<br>
<br>

### `POST`

Creates a new user that can now use the system. Also returns a valid login token meaning the user is now logged in after sign up.  
Will error if there is a duplicate username or password (the user already exists)

**Required Data:**

```
{
    email: (string),
    name: (string),
    username: (string),
    password: (string)
}
```

**Data Returned**

```
{
    user_id: (number),
    token: (string)
}
```

<br>
<br>

### `PATCH`

Modify an existing user if you have a valid token. Note that the token is sent as a header.

**Required Headers:**

```
{
    token: (string)
}
```

**Optional Data:** Send 1 or more of these to update the client that owns the given token

```
{
    email: (string),
    name: (string),
    profile_photo:? (string),
    username: (string),
    bio: (string),
    links: (string),
    phone_number: (string),
    date_of_birth (number)
    
}
```

**No Data Returned**

<br>
<br>

### `DELETE`

Delete an existing user if you have a valid token and password. Note that the token is sent as a header.

**Required Headers:**

```
{
    token: (string)
}
```

**Required Data:**

```
{
    password: (string)
}
```

**No Data Returned**

<br>
<br>

## `User-Sensative`
**URL: http://127.0.0.1:5000/api/user-sensative**  
Supported HTTP Methods: **get,**

### `GET`

gets all the users info,

**Required Params:**

```
{
    token: (string)
}
```

**Data Returned**

```
{
    email: (string),
    name: (string),
    profile_photo:? (string),
    username: (string),
    password: (string),
    bio: (string),
    links: (string),
    phone_number: (string),
    date_of_birth (number)
}
```

<br>
<br>

## `User-Login`

**URL: http://127.0.0.1:5000/api/user-login**  
Supported HTTP Methods: **POST, DELETE**

### `POST`

Log a user in. Will error if the email / password don't exist in the system.

**Required Data:**

```
{
    email: (string),
    password: (string)
}
```

**Data Returned**

```
{
    client_id: (number),
    token: (string)
}
```

<br>
<br>

### `DELETE`

Delete an existing token. Will error if the token sent does not exist.

**Required Headers:**

```
{
    token: (string)
}
```

**No Data Returned**

<br>
<br>

## `User-upload`

**URL: http://127.0.0.1:5000/api/user-upload**  
Supported HTTP Methods: **GET, POST, PATCH, DELETE**

### `GET`

Returns information about a single user-upload , will error if the upload_id does not exist.

**Required Params:**

```
{
    token: (string)  display favourties as a feed
}
```

**Data Returned**

```
{
    title: (string),
    description: (string),
    upload_id: (number)
    created_at: (string)
}
```

<br>
<br>

### `POST`

Adds a new upload from the user. Must be logged in as the user to send the correct token.

**Required headers:**

```
{
    token: (string),
}
```

Required Data:

```
{
    title: (string),*
    image_ref: (string),*
    description: (string), optional?
    created_at: (string)
}
```

<br>
<br>

### `PATCH`

Modify an existing upload if you have a valid token. Note that the token is sent as a header.

**Required Headers:**

```
{
    token: (string)
}
```

**required data**
```
{
    upload_id: (string)
}
```

**Optional Data:** Send 1 or more of these to update the upload that owns the given token

```
{
    title: (string), optional
    description: (string), optional
}
```

**No Data Returned**

<br>
<br>

### `DELETE`

Delete an existing upload if you have a valid token. Note that the token is sent as a header.

**Required Headers:**

```
{
    token: (string)
}
```

**No Data Returned**
<br>
<br>

## `Users-Comments`
**URL: http://127.0.0.1:5000/api/users-comments**  
Supported HTTP Methods: **GET**

### `GET`

Returns all the comments associated with the upload,

**Required Params:**

```
{
    upload_id: (int)
}
```

Data Returned:

```
{
    user_id: (int)
    comments: (string)
}
```

### `POST`

Returns all the comments associated with the upload,

**Required headers:**

```
{
    token: (string),

}
```

Data Required:

```
{
    upload_id: (int)
    comments: (string)
}
```


### `PATCH`

Returns all the comments associated with the upload,

**Required Params:**

```
{
    token: (string),
    upload_id: (int)
}
```

Data Returned:

```
{
    comments: (string)
}
```

### `DELETE`

Returns all the comments associated with the upload,

**Required Headers:**

```
{
    upload_id: (int),
    token: (string)
}
```

<br>
<br>

## `Upload-Tags`
**URL: http://127.0.0.1:5000/api/upload-tags**  
Supported HTTP Methods: **GET,POST,PATCH,DELETE**

### `GET`

Returns information about specific user-comment,

**Required Params:**

```
{
    upload_id: (int),
}
```

Retunedred Data:

```
{
    tag.id: (int),
    tags: (string)
}
```


<br>
<br>

### `POST`

Adds a new tag to a upload,

**Required Headers:**

```
{
    upload_id: (int),
    token: (string)
}
```

Required Data:

```
{
    tag: (string)
}
```

**No Data Returned:**

<br>
<br>

### `DELETE`

Deletes an existing tag for an upload,

**Required Headers:**

```
{
   
    token: (string)
}
```

**Required Data**
```
{
    (tag)id: (int)
}
```

<br>
<br>

## `Favourite`
**URL: http://127.0.0.1:5000/api/favourite**  
Supported HTTP Methods: **GET,POST,DELETE**

### `GET`

Returns the users favourites as a feed,

**Required Params:**

```
{
    token: (string)
}
```

Retunedred Data:

```
{
    favourite_user_upload_id's
}
```


<br>
<br>

### `POST`

favourites an upload,

**Required Headers:**

```
{

    token: (string)
}
```

Required Data:

```
{
    upload_id: (int),
}
```

**No Data Returned:**

<br>
<br>

### `DELETE`

Deletes an existing favourite, 

**Required Headers:**

```
{
   
    token: (string)
}
```

```
{
    upload_id: (int)
}
```

**No Data Returned**

<br>
<br>

## `following`
**URL: http://127.0.0.1:5000/api/follow**  
Supported HTTP Methods: **GET,POST,DELETE**

### `GET`

Returns the users is following,

**Required Params:**

```
{
    token: (string)
}
```

Retunedred Data:

```
{
    user_id: (int)
}
```

<br>
<br>

### `POST`

shows if you followed a user,

**Required Headers:**

```
{
    token: (string)
}
```

Required Data:

```
{
 user_id: (int),
}
```

**No Data Returned:**

<br>
<br>

### `DELETE`

stops following a user,

**Required Headers:**

```
{
    token: (string)
}
```

Required Data:

```
{
 user_id: (int),
}
```

**No Data Returned**

<br>
<br>

## `followed-by`
**URL: http://127.0.0.1:5000/api/followed**  
Supported HTTP Methods: **GET**

### `GET`

Returns who the user is followed by as a feed,

**Required Params:**

```
{
    token: (string)
}
```

Retunedred Data:

```
{
    user_id: (int)
}
```
<br>
<br>