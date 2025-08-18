release: python manage.py collectstatic --noinput
web: gunicorn wafadash.wsgi --bind 0.0.0.0:$PORT
