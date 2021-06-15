INSERT INTO givestrapi_persontype (description)
VALUES (
    'Need Strength'
  );

SELECT * from givestrapi_person
SELECT latitude, longitude from givestrapi_person

delete from givestrapi_persontype where id=3

delete from auth_user where id=13

update auth_user set first_name = "Scott"
where id=10

update givestrapi_person set street = "1401 3rd Ave N" where id=6

update givestrapi_person
set
latitude = 36.168573  ,
longitude = -86.737487
where id=5


INSERT INTO givestrapi_day (description)
VALUES (
    'Need Strength'
  );
