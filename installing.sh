apt-get install python3-dev
python3.9 -m pip install -r requirements_local.txt
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py runserver
