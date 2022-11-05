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
    email: (string),
    phone_number: (string),?
    date_of_birth: (string),?
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
    created_at: (string)
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
    password: (string),
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

## `User-Login`

**URL: http://127.0.0.1:5000/api/user-login**  
Supported HTTP Methods: **POST, DELETE**

### `POST`

Log a client in. Will error if the email / password don't exist in the system.

**Required Data:**

```
{
    email: (string),
    password: (string)
    created_at: (string)??
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

Returns information about a single user-upload, will error if the upload_id does not exist.

**Required Params:**

```
{
    upload_id: (number)
}
```

**Data Returned**

```
{
    title: (string),
    image_ref: (string),
    description: (string),
    comments: (string), ?
    favourite: (string), ?
    tags: (string), ?
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
    tags: (string), optional?
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

**Optional Data:** Send 1 or more of these to update the upload that owns the given token

```
{
    title: (string), optional
    description: (string), optional
    tags: (string) optional
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

