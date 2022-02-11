# File storage API

REST API for uploading and retrieving files built with Django and Django Rest Framework

## API Documentation

### Overview

The File Storage API provides quick and simple way to upload, retrieve and delete files using conventional HTTP requests. It currently supports only images.

### Authentication

In order to interact with File Storage API, you or your application must authenticate.

The File Storage API handles this through Token Authentication.

To generate your Token, send a POST request to <code>/api/v1/accounts/token/</code>. The <code>username</code> and <code>password</code> must be provided as body parameter.

**Payload**

```json
{
  "username": "admin",
  "password": "adminadmin"
}
```

**Responses**

<code style="color: green">200</code> - OK

```json
{
  "token": "0bc07b64cea678ca534520a69f5bc306ecb43aa3"
}
```

<code style="color: red">400</code> - Bad Request

```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

<code style="color: red">405</code> - Method Not Allowed

```json
{
  "detail": "Method \"GET\" not allowed."
}
```

#### How to authenticate with obtained token

In order to make an authenticated request, include an <code>Authorization</code> header containing your auth token. All requests must be made over HTTPS.

**Header example**

```
Authorization: Token 0bc07b64cea678ca534520a69f5bc306ecb43aa3
```

### Resources

#### <code style="background-color: green; color: white;" >GET</code> List all images

*Authorizations: Token Authentication*

In order to list all images on your account, send GET request to <code>/api/v1/files/image/</code>.

**Responses**

<code style="color: green">200</code> - OK

```json
[
  {
    "pk": 1,
    "owner": 1,
    "image": "https://sobolevmax.pythonanywhere.com/media/uploads/iphone-13-pro-max-graphite-select_46vxZdA.jpeg"
  },
  {
    "pk": 2,
    "owner": 1,
    "image": "https://sobolevmax.pythonanywhere.com/media/uploads/myd82ya1_FccZegQ.png"
  }
]
```

<code style="color: red">401</code> - Unauthorized

```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### <code style="background-color: blue; color: white;" >POST</code> Upload an image

*Authorizations: Token Authentication*

To upload an image, send POST request to <code>/api/v1/files/image/</code> with your image under the key <code>image</code>.

**Responses**

<code style="color: green">201</code> - Created

```json
{
    "pk": 7,
    "owner": 1,
    "image": "https://sobolevmax.pythonanywhere.com/media/uploads/iphone-13-pro-max-graphite-select_46vxZdA_qOd8Ole.jpeg"
}
```

<code style="color: red">401</code> - Unauthorized

```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### <code style="background-color: green; color: white;" >GET</code> Retrieve specific image

*Authorizations: Token Authentication*

In order to retrieve a specific image by it's <code>pk</code> (primary key), send GET request to <code>/api/v1/files/image/[pk]/</code>.

**Responses**

<code style="color: green">200</code> - OK

```json
{
    "pk": 7,
    "owner": 1,
    "image": "https://sobolevmax.pythonanywhere.com/media/uploads/iphone-13-pro-max-graphite-select_46vxZdA_qOd8Ole.jpeg"
}
```

<code style="color: red">401</code> - Unauthorized

```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### <code style="background-color: red; color: white;" >DELETE</code> Delete an image

*Authorizations: Token Authentication*

To delete an existing image, send DELETE request to <code>/api/v1/files/image/[pk]/</code>.

**Responses**

<code style="color: green">204</code> - No Content

```
```

<code style="color: red">401</code> - Unauthorized

```json
{
  "detail": "Authentication credentials were not provided."
}
```




