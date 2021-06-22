# `GIVE YOUR STRENGTH`

This is my backend NSS capstone project designed to implement a full stack React to Python/Django app with maps.
#
## `What is GYS?`

![GYS Logo](https://res.cloudinary.com/dp6mbc90b/image/upload/v1624373214/gyslogoboth_jfkhle.jpg)

Ths idea behind GYS is based on my time as a caretaker and realizing the important need for physical strength. I thought to myself, it would be quite handy to know if someone near me was in need. Whether that's to get in and out of bed, to get up from a fall, or even to carry some groceries inside.

Users sign up as Giving or Needing strength. Their addresses are geocoded. Select themselves as available. Then a map is rendered of users within a certain distance of their geocoded address.

The app is not unlike other apps. We capture user data, put it in a database, pull that data back out, and put it on a map. It's a simple app, but was a challenge nonetheless.
#
## `Tech Used`
- React
- React Leaflet Maps
- React Bootstrap
- Django (server side)
- Python (server side)
- sqlLite (server side)
- Distance calculation in Python
- Geocoding using Nominatim
#
Front end: https://github.com/blusanders/givestrength
#

## `API Setup`

- Clone this repository and change to the directory in the terminal.
- Run pipenv shell
- Run pipenv install
- Type this exact thing into the terminal to run the migrations and seed the database: ./seed_data.sh#
- run python manage.py runserver
#
![GYS Map](https://res.cloudinary.com/dp6mbc90b/image/upload/v1624373547/gysstrengthmap_zmpijr.png)

#

## `ERD`
https://dbdiagram.io/d/60ac2191b29a09603d165542

#

## `Figma Wireframe`
https://www.figma.com/file/iMfDRulzT6WaagSkCeWA0U/Give-Your-Strength?node-id=0%3A1

#

## `Wishlist`
Lots of things I'd want to add to this down the road:

- Messaging between users
- Routing (from person to person)
- Scheduling
- Change the look and feel of the map
- Equipment loan
