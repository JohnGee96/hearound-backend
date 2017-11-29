# Project Hearound API Documentations

### GET /api/posts
Retrieves all posts

Example request: 

    curl -X GET http://<Server_IP>/api/posts

Example Response: 

    {
        "num_results": 5, 
        "objects": [
            {
                "body": "This is the geolocation of Boston", 
                "created_at": "2017-10-30T23:51:21", 
                "id": 1, 
                "lat": 42.3639457, 
                "lng": -71.0569078, 
                "title": "Boston", 
                "updated_at": "2017-10-30T23:54:12"
            }, 
            {
                "body": "This is the geolocation of New York", 
                "created_at": "2017-10-31T00:40:23", 
                "id": 2, 
                "lat": 40.7137746, 
                "lng": -74.0060504, 
                "title": "New York", 
                "updated_at": "2017-10-31T00:49:39"
            }, 
            {
                "body": "This is the geolocation of Los Angeles", 
                "created_at": "2017-10-31T00:42:50", 
                "id": 3, 
                "lat": 34.055588, 
                "lng": -118.2283376, 
                "title": "Los Angeles", 
                "updated_at": "2017-10-31T00:42:50"
            }, 
            {
                "body": "This is the geolocation of London", 
                "created_at": "2017-10-31T00:45:01", 
                "id": 4, 
                "lat": 51.5076913, 
                "lng": -0.1288709, 
                "title": "London", 
                "updated_at": "2017-10-31T00:45:01"
            }, 
            {
                "body": "This is the geolocation of Hillside", 
                "created_at": "2017-10-31T00:47:00", 
                "id": 5, 
                "lat": 42.4088871, 
                "lng": -71.1196583, 
                "title": "Hillside Apartments", 
                "updated_at": "2017-10-31T00:47:00"
            }
        ], 
        "page": 1, 
        "total_pages": 1
    }

### GET /api/posts/#
Retrieves a post with id #.

Example request: 

    curl -X GET http://<Server_IP>/api/posts/1

Example Response:

    {
        "body": "This is the geolocation of Boston", 
        "created_at": "2017-10-30T23:51:21", 
        "id": 1, 
        "lat": 42.3639457, 
        "lng": -71.0569078, 
        "title": "Boston", 
        "updated_at": "2017-10-30T23:54:12"
    }

### GET /api/users 
Retrieves all users with their email and the posts they created

Example request:

    curl -X GET http://<Server_IP>/api/users

Example Response:

    {
        "num_results": 4, 
        "objects": [
            {
            "email": "ssmith@smith.com", 
            "id": 1, 
            "post": [
                {
                "id": 1
                }, 
                {
                "id": 2
                }
            ], 
            "username": "Ssmith"
            }, 
            {
            "email": "kon.kin@kin.com", 
            "id": 2, 
            "post": [], 
            "username": "kkin"
            }, 
            {
            "email": "john.kurt@kurt.com", 
            "id": 3, 
            "post": [], 
            "username": "jkurt"
            }, 
            {
            "email": "kate.lin@kate.com", 
            "id": 4, 
            "post": [], 
            "username": "jlin"
            }
        ], 
        "page": 1, 
        "total_pages": 1
    }

### POST /api/signup
Register a new user. Supply the following JSON in the POST request

    {
        "email": "example@ex.com"
        "username": "user1"
        "password": "some_password"
    }

Example Request:

    curl -H "Content-Type: application/json" -X POST -d '{ "email": "example@ex.com","username": "user1","password":"some_password"}' http://<Server_IP>/api/signup

Example Response:

    {
        "email": "example@ex.com", 
        "user_id": 0, 
        "username": "user1"
    }

### POST /api/login
Authenticate a existing user. Supply the following JSON in the request

    {
        "email": "example@ex.com"
        "password": "some_password"
    }

Example Request

    curl -H "Content-Type: application/json" -X POST -d '{ "email": "example@ex.com","password":"some_password"}' http://<Server_IP>/api/login

Example Response:

    {
        "email": "example@ex.com", 
        "user_id": 0, 
        "username": "user1"
    }

### POST /api/nearby_posts
Retrieve posts within a fixed radius around a geolocation. Must provide a POST request with the following
JSON format:

    {
        "lat": 42.408226
        "lng": -71.115944
        "radius": 5  #in kilometer
    }

Example request:

    curl -H "Content-Type: application/json" -X POST -d '{ "lat": 42.408226, "lng": -71.115944, "radius": 5}' http://<Server_IP>/api/nearby_posts

Example Response:

    [
        {
            "body": "This is the geolocation of Hillside", 
            "id": 5, 
            "lat": 42.4088871, 
            "lng": -71.1196583, 
            "modified_at": [
            "2017-10-31", 
            "00:47:00"
            ], 
            "title": "Hillside Apartments", 
            "updated_at": [
            "2017-10-31", 
            "00:47:00"
            ]
        }, 
        {
            "body": "This is the geolocation of Halligan", 
            "id": 6, 
            "lat": 42.408226, 
            "lng": -71.115944, 
            "modified_at": [
            "2017-10-31", 
            "01:08:39"
            ], 
            "title": "Halligan Hall", 
            "updated_at": [
            "2017-10-31", 
            "01:08:39"
            ]
        }
    ]

### POST /api/nearby_post_locations
Retrieve the coordinates of nearby posts in a json format Must provide a POST request with the following
JSON format:

    {
        "lat": 42.408226
        "lng": -71.115944
        "radius": 5  #in kilometer
    }

Example request:

    curl -H "Content-Type: application/json" -X POST -d '{ "lat": 42.408226, "lng": -71.115944, "radius": 5}' http://<Server_IP>/api/nearby_post_locations

Example Response:

    {
        "features": [
            {
            "geometry": {
                "coordinates": [
                -71.1196583, 
                42.4088871
                ], 
                "type": "Point"
            }, 
            "properties": {
                "author": "John Smith"
            }, 
            "type": "Feature"
            }, 
            {
            "geometry": {
                "coordinates": [
                -71.115944, 
                42.408226
                ], 
                "type": "Point"
            }, 
            "properties": {
                "author": "John Smith"
            }, 
            "type": "Feature"
            }
        ], 
        "type": "FeatureCollection"
    }


### POST /api/posts
Create a new post by providing a POST request with following JSON format:

    {
        "title": "Sample Post",
        "body": "This the body of a sample post", 
        "lat": 42.408226
        "lng": -71.115944
    }

Example request:

    curl -H "Content-Type: application/json" -X POST -d '{"title":"Sample Post", "body": "This the body of a sample post", "lat": 42.408226, "lng": -71.115944}' http://<Server_IP>/api/posts

### PUT /api/posts/#
Update the Post with id #. Provide the PUT request with the following JSON:

    {
        "title": "Sample Post",
        "body": "This will replace the body of the original Sample Post", 
        "lat": 42.408226
        "lng": -71.115944
    }


Example request:

    curl -H "Content-Type: application/json" -X PUT -d '{"title":"Sample Post", "body": "This will replace the body of the original Sample Post", "lat": 42.408226, "lng": -71.115944}' http://<Server_IP>/api/posts/1
