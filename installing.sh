python3.9 -m venv env
source env/bin/activate
python3.9 -m pip install --upgrade pip
dnf install python3-devel
echo "finished installing python3-dev"
python3.9 -m pip install -r requirements_local.txt
python3.9 manage.py collectstatic --noinput
