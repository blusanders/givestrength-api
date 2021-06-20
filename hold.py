print(
            latlong,
            getDistance(
            fromAddress[0],
            fromAddress[1],
            helpArray[latlong][0],
            helpArray[latlong][1]
            ))


bio: "Bio here"
city: "El Paso"
email: "jd@jd.com"
first_name: "Jane"
last_name: "Doe"
password: "123"
person_type_id: "1"
popup: "Popup here"
state: "TX"
street: "5121 Camino de la Vista"
username: "jane"
zip: "79932"

{
	"bio": "Test for delete",
	"city": "Nashville",
	"email": "tt@tt.com",
	"first_name": "Five",
	"last_name": "Fiverson",
	"password": "333",
	"person_type_id": 1
	"popup": "Test me!",
	"state": "TN",
	"street": "2712 Deerfield Dr",
	"username": "555",
	"zip": "37208",
	"phone": "6155550000",
}



https://nominatim.openstreetmap.org/search?q=830+Windhurst+San+Antonio+TX&format=geojson





def getHelp() :
    from_address = [36.17915, -86.75908] #logged in user

    #all TN addresses
    #ask Will about filtering data first
    #searching all addresses not realistic
    help_array = [
        [36.17213, -86.75485], #.53
        [36.1844, -86.74291], #.96
        [36.18869, -86.76962], #.88	
        [36.196770, -86.745057] #1.44
    ]

    distance=1
    within_distance = []

    for latlong in range(len(help_array)):
        distance_away = get_distance(
        from_address[0],
        from_address[1],
        help_array[latlong][0],
        help_array[latlong][1]
        )
        if distance_away<=distance:
            within_distance.append(help_array[latlong])
    print(within_distance)


def destroy(self, request, pk=None):
        """Handle DELETE requests for a story
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            story = Story.objects.get(user=request.auth.user,pk=pk)
            story.delete()