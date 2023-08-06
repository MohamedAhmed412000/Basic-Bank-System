python3 --version
pip install venv
python -m venv env
env\scripts\activate
pip install -r requirements_local.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
