release: python olympics/manage.py migrate
release: echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell
web: gunicorn --chdir olympics olympics.wsgi — log-file -
