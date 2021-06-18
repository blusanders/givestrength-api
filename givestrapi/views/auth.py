from givestrapi.views.person import geo_get
import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from givestrapi.models import Person


@csrf_exempt
def login_user(request):
    '''Handles the authentication of a person

    Method arguments:
        request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            token = Token.objects.get(user=authenticated_user)
            person = Person.objects.get(user=authenticated_user)
            data = json.dumps({
                "valid": True,
                "token": token.key,
                "lat": person.latitude,
                "long": person.longitude
            })
            return HttpResponse(data, content_type='application/json')

        else:
            # Bad login details were provided. So we can't log the user in.
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type='application/json')


@csrf_exempt
def register_user(request):
    '''Handles the creation of a new person for authentication

    Method arguments:
        request -- The full HTTP request object
    '''

    req_body = json.loads(request.body.decode())

    new_user = User.objects.create_user(
        username=req_body['username'],
        email=req_body['email'],
        password=req_body['password'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    latLong = geo_get(
        req_body['street'],
        req_body['city'],
        req_body['state'],
        req_body['zip'],
        )
    lat = latLong[1]
    long = latLong[0]

    print(lat,long)

    person = Person.objects.create(
        user=new_user,
        bio=req_body['bio'],
        popup=req_body['popup'],
        street=req_body['street'],
        city=req_body['city'],
        state=req_body['state'],
        zip=req_body['zip'],
        phone=req_body['phone'],
        latitude=lat,
        longitude=long,
        person_type_id=req_body['person_type_id']
    )

    # Commit the user to the database by saving it
    person.save()

    # Use the REST Framework's token generator on the new user account
    token = Token.objects.create(user=new_user)

    # Return the token to the client
    data = json.dumps({"token": token.key})
    return HttpResponse(data, content_type='application/json')
