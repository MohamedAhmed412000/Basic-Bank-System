ls ../..
echo "finished first ls"
ls ../../bin
echo "finished second ls"
python3.9 -m venv env
source env/bin/activate
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements_local.txt
python3.9 manage.py collectstatic --noinput
