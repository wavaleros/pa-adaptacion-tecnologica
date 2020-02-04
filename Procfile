release: python olympics/manage.py migrate
web: gunicorn --chdir olympics olympics.wsgi — log-file -
