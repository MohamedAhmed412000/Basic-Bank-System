python3 --version
python3 -m venv env
source env\scripts\activate
python3 -m pip install -r requirements_local.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
