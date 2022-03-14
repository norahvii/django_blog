A blog but in Django

mkvirtualenv --python=python3.7 myblog
pip install -U django==2.0

python manage.py migrate
python manage.py makemigrations blog
python manage.py migrate

python manage.py createsuperuser

copy wsgi file to /var/www

source code:
/home/norahvii/django_blog/mysite

working directory:
/home/norahvii/

wsgi config file:
/var/www/norahvii_pythonanywhere_com_wsgi.py

virtualenv:
/home/norahvii/.virtualenvs/myblog

static files:
url:
/static/admin
directory:
/home/norahvii/.virtualenvs/myblog/lib/python3.7/site-packages/django/contrib/admin/static/admin

url:
/static
directory:
/home/norahvii/django_blog/mysite/blog/static
