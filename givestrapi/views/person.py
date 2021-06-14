"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from givestrapi.models import PersonType
from django.contrib.auth.models import User

class Person(ViewSet):
    """Give Your Strength Person"""

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

        person_type = PersonType.objects.get(pk=request.data["personTypeId"])
        person.person_type = person_type

        try:
            person.save()
            serializer = PersonSerializer(person, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handle GET requests for a person

        Returns:
            Response -- JSON serialized person instance
        """
        try:
            #http://localhost:8000/person/2
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person, context={'request': request})
            return Response(serializer.data,)

        except Exception as ex:
            return HttpResponseServerError(ex, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a Person

        Returns:
            Response -- Empty body with 204 status code
        """

        person = Person.objects.get(pk=pk)

        person.user.first_name = request.data["firstName"]
        person.user.email = request.data["email"]
        person.user.last_name = request.data["lastName"]

        person.street = request.data["street"]
        person.city = request.data["city"]
        person.state = request.data["state"]
        person.zip = request.data["zip"]
        person.phone = request.data["phone"]
        person.bio = request.data["bio"]
        person.popup = request.data["popup"]
        person.latitude = request.data["latitude"]
        person.longitude = request.data["longitude"]
        person.person_type_id = request.data["person_type_id"]

        person.user.save()
        person.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

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

    def list(self, request):
        """Handle GET requests to person resource

        Returns:
            Response -- JSON serialized list of peopel within a given distance
        """
        #get all people, filter by distance
        user = Person.objects.get(user=request.auth.user)
        person = Person.objects.all()
        # geo = getGeo(street, city, state, zip)
        # print("GEO: "+geo)

        #    http://localhost:8000/person?distance=1

        distance = self.request.query_params.get('distance', None)
        if distance is not None:
            person_filtered = person.filter(gametype__id=game_type)


        serializer = PersonSerializer(
            games, many=True, context={'request': request})
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'is_staff', 'is_active', 'email')

class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Person
        fields = (
            'id', 
            'user',
            'address',
            'city',
            'state', 
            'zip', 
            'phone', 
            'bio',
            'popup',
            'latitude', 
            'longitude'
        )

def getGeoDistance(lat1,lat2,lat3,lat4):
    return "HELLO"

