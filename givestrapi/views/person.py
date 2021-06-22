"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from django.db.models.query_utils import select_related_descend
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from givestrapi.models import Person, PersonType, Availability, availability
from django.contrib.auth.models import User
import urllib.request
import json
import math

class PersonViewSet(ViewSet):
    """Give Your Strength Person"""


#****************************
# add ONE person
#****************************

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Person instance
        """

        user = Person.objects.get(user=request.auth.user)

        person = Person()
        person.street = request.data["street"]
        person.city = request.data["city"]
        person.state = request.data["state"]
        person.zip = request.data["zip"]
        person.bio = request.data["bio"]
        person.popup = request.data["popup"]
        person.latitude = request.data["latitude"]
        person.longitude = request.data["longitude"]

        person_type = PersonType.objects.get(pk=request.data["person_type_id"])
        person.person_type = person_type

        try:
            person.save()
            serializer = PersonSerializer(person, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


#****************************
# get ONE person
#****************************

    def retrieve(self, request, pk=None):
        """Handle GET requests for a person

        Returns:
            Response -- JSON serialized person instance
        """
        try:
            #http://localhost:8000/person/2
            if int(pk)==0:
                person = Person.objects.get(user=request.auth.user)

            else:
                person = Person.objects.get(pk=pk)

            serializer = PersonSerializer(person, context={'request': request})
            return Response(serializer.data,)

        except Exception as ex:
            return HttpResponseServerError(ex, status=status.HTTP_404_NOT_FOUND)


#****************************
# update ONE person
#****************************

    def update(self, request, pk=None):
        """Handle PUT requests for a Person

        Returns:
            Response -- Empty body with 204 status code
        """
        person = Person.objects.get(user=request.auth.user)
        
        selected_days = request.data["selected_days"]

        if selected_days:
            print(selected_days)
            selected_days_array = []

            person.availability_set.all().delete()

            for x in selected_days:

                    z = x["value"]
                    selected_days_array.append(z)

                    y = Availability()
                    y.day_id = x["value"]
                    y.person = person
                    y.save()

            print("sd: ", selected_days_array)

        # person = Person.objects.get(pk=pk)

            
        # if selected_days_array:
        #     person.availability_set = selected_days_array
        
        person.user.first_name = request.data["first_name"]
        person.user.last_name = request.data["last_name"]
        person.user.email = request.data["email"]
        person.user.username = request.data["username"]

        print(request.data["username"])
        
        person.street = request.data["street"]
        person.city = request.data["city"]
        person.state = request.data["state"]
        person.zip = request.data["zip"]
        person.phone = request.data["phone"]
        person.on_call = request.data["on_call"]
        person.bio = request.data["bio"]
        person.popup = request.data["popup"]

        latlong = geo_get(
            request.data["street"],
            request.data["city"],
            request.data["state"],
            request.data["zip"],
        )

        # print("latlong: ", latlong)

        person.latitude = latlong[1]
        person.longitude = latlong[0]
        person.person_type_id = request.data["person_type_id"]

        person.user.save()
        person.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


#****************************
# delete ONE person
#****************************

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single person

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            person = Person.objects.get(pk=pk)
            person.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Person.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#****************************
# get ALL people
#****************************

    def list(self, request):
        """Handle GET requests to person resource

        Returns:
            Response -- JSON serialized list of people within a given distance
        """
        #get all people, filter by distance
        current_user = Person.objects.get(user=request.auth.user)
        
        #get all people w distances. Zero distance = logged in user.
        


        person = Person.objects.filter(on_call=True)
        # person = Person.objects.all()

        # person = Person.objects.filter(availability__day__id=2)
        # tues wed 2,3
        # person = Person.objects.filter(availability__day__id__in=array)
        
        # avail = Availability.objects.filter(day_id=1)
        # print(person)

        # Thing.objects.filter(field__in=Another_Thing.object.filter())

        #get all markers within distance except logged in use
        # person = Person.objects.exclude(user=request.auth.user)

        #calc distance bet lat/long and logged in user lat/long
        #http://localhost:8000/person?distance=1

        distance = self.request.query_params.get('distance', None)

        if distance is not None:

            def distance_filter(person):
                from_lat = current_user.latitude
                from_long = current_user.longitude
                to_lat = person.latitude
                to_long = person.longitude

                #distance bet each user and the logged in user
                distance_bet = get_distance(from_lat, from_long, to_lat, to_long)
                # print(person.id, person.user.first_name, distance_bet)
                person.distance = distance_bet
                
                if (distance_bet<=float(distance)):
                    return True
                return False

            person = filter(distance_filter, person)

        serializer = PersonSerializer(
            person, many=True, context={'request': request})
        return Response(serializer.data)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'is_staff', 'is_active', 'email')

class PersonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonType
        fields = ['id','description']

class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    person_type = PersonTypeSerializer(many=False)

    class Meta:
        model = Person
        fields = (
            'id', 
            'user',
            "person_type",
            'street',
            'city',
            'state', 
            'zip', 
            'phone', 
            'bio',
            'popup',
            'on_call',
            'latitude', 
            'longitude',
            "distance",
            "availability_set",
        )
        depth = 2


def get_distance(from_lat,from_long, to_lat, to_long):

    #takes to and from lat/long
    #returns distance in miles bet those points

    radius = 6371  # km

    dlat = math.radians(to_lat - from_lat)
    dlon = math.radians(to_long - from_long)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(from_lat)) * math.cos(math.radians(to_lat)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    d = d*.62 #returns miles
    return d


def geo_get(street, city, state, zip):

    q = f"{street} {city} {state} {zip}"
    q = q.replace(" ", "+")

    fetchURL = f"https://nominatim.openstreetmap.org/search?q={q}&format=geojson"
    # print("fetch: ", fetchURL)
    contents = urllib.request.urlopen(fetchURL).read()

    JSON_object = json.loads(contents)
    
    # try:
    #     lat = JSON_object['features'][0]['geometry']['coordinates'][0]
    # except IndexError:
    #     gotdata = 'null'
    
    # if gotdata:
    #     lat = JSON_object['features'][0]['geometry']['coordinates'][0]
    #     long = JSON_object['features'][0]['geometry']['coordinates'][1]
    # else:   
    #     lat = ""
    #     long = ""

    if len(JSON_object['features'])>0:
        lat = JSON_object['features'][0]['geometry']['coordinates'][0]
        long = JSON_object['features'][0]['geometry']['coordinates'][1]
    else:   
        lat = ""
        long = ""

    return [lat,long] 

