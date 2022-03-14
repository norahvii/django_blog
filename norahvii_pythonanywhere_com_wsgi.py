# +++++++++++ DJANGO +++++++++++
import os
import sys

path = '/home/norahvii/django_blog/mysite/'
if path not in sys.path:
    sys.path.append(path)
os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")

import django
django.setup()

#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
