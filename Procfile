server: gunicorn config.wsgi:application
worker: python manage.py celery worker --loglevel=info
flower: python manage.py celery flower --loglevel=info
beater: python manage.py celery beat --loglevel=info