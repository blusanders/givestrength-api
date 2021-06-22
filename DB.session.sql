select
p.id,
p.user_id,
u.first_name,
p.latitude,
p.longitude,
p.city,
p.bio,
p.on_call,
p.person_type_id
from givestrapi_person p
join auth_user u on u.id = p.user_id
order by p.city, person_type_id

select * from givestrapi_person where id=17

update givestrapi_person set on_call=true where id=17

select * from auth_user

select * from authtoken_token

select * from givestrapi_availability 

select * from givestrapi_day

select * from givestrapi_availability a


insert into givestrapi_availability (day_id, person_id)
values (5,6)

delete from auth_user where id=18 or id=19 or id=49

delete from authtoken_token where
user_id=13 or
user_id=19 or
user_id=20

delete from givestrapi_person where id=13

update givestrapi_person set latitude=36.230922 , longitude=-86.720145
where id=3

update givestrapi_person set
bio="Hi everyone. I could use some help getting in and out of bed 3 days a week."
where id=14

update givestrapi_person set person_type_id = 2 where id=16


select a.* from givestrapi_availability a

select a.* from givestrapi_availability a
join givestrapi_person p on a.person_id = p.id
where a.day_id = 2
