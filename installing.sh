python -m venv env
pip install -r requirements_local.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
