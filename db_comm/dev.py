from db_comm.settings import *

DEBUG = True
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.farmers1',
    }
}
