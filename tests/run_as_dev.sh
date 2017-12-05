# This is the script that initialize the backend code

# dependencies
echo Installing dependencies...

pip install -r requirements.txt

echo Dependencies installed

# run app
echo Running app...

#PYTHONPATH=. python -u tests/app.py
tox -e py27 -- --cov=graphene_bottle
