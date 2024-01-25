run:
python3 manage.py runserver xxx.xx.xx.xxx:xxxx

Optionally use nginx (or similar) and gunicorn
gunicorn -c gunicorn.py ask.wsgi:application
