release: python manage.py migrate
web: gunicorn wafadash.wsgi --bind 0.0.0.0:$PORT