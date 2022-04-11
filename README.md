A blog but in Django.

Up and running here: http://norahvii.pythonanywhere.com/

## CLI Setup:
* `mkvirtualenv --python=python3.7 myblog`
* `pip install -U django==2.0`
* `python manage.py migrate`
* `python manage.py makemigrations blog`
* `python manage.py migrate`
* `python manage.py createsuperuser`
* `copy wsgi file to /var/www`

## Pythonanywhere Setup:
source code:
* `/home/norahvii/django_blog/mysite`

working directory:
* `/home/norahvii/`

wsgi config file:
* `/var/www/norahvii_pythonanywhere_com_wsgi.py`

virtualenv:
* `/home/norahvii/.virtualenvs/myblog`

## Static files:
url:
* `/static/admin`

directory:
* `/home/norahvii/.virtualenvs/myblog/lib/python3.7/site-packages/django/contrib/admin/static/admin`

url:
* `/static`

directory:
* `/home/norahvii/django_blog/mysite/blog/static`
