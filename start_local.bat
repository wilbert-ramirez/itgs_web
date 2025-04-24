@echo off
call env\Scripts\activate.bat
set DJANGO_SECRET_KEY=local-secret-key
set DJANGO_DEBUG=True
set DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
python manage.py migrate
python manage.py runserver