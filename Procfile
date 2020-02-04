release: python olympics/manage.py migrate
release: python olympics/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
web: gunicorn --chdir olympics olympics.wsgi — log-file -
