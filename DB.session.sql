select
p.id,
p.user_id,
u.first_name,
p.latitude,
p.longitude,
p.city,
p.person_type_id
from givestrapi_person p
join auth_user u on u.id = p.user_id
order by p.city, person_type_id

select * from givestrapi_person
select * from auth_user
select * from authtoken_token

delete from auth_user where id=18 or id=19 or id=43

delete from authtoken_token where
user_id=13 or
user_id=19 or
user_id=20

delete from givestrapi_person where id=13

update givestrapi_person set latitude=36.230922 , longitude=-86.720145
where id=3

update givestrapi_person set person_type_id = 2 where user_id=44

