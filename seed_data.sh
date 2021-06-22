rm db.sqlite3
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata availabilty
python manage.py loaddata day
python manage.py loaddata gender
python manage.py loaddata message
python manage.py loaddata person
python manage.py loaddata person_type