import os
from .base import *

#Added comment by LNguyen - Set service name to BASE_SITE_URL ie., https://fullservername
BASE_SITE_URL = 'https://rapidpivot.com'
AMQP_URL = 'amqp://guest:guest@localhost:5672//'

#Added comment by LNguyen - Update with server name and IP addresse ie., [<servername', '127.0.0.1]
ALLOWED_HOSTS = ['rapidpivot.com']

#Update with admin email address ie., Rapid@gmail.com
ADMINS = (('Name', 'email@service.com'),)

DEBUG = False
TEMPLATE_DEBUG = False

#original commented outed by LNguyen
#DEBUG = True
#TEMPLATE_DEBUG = True

# SSL/TLS Settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
os.environ['wsgi.url_scheme'] = 'https'

# Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = retrieve_secret_configuration("EMAIL_HOST")
EMAIL_HOST_USER = retrieve_secret_configuration("EMAIL_USER")
EMAIL_HOST_PASSWORD = retrieve_secret_configuration("EMAIL_PASS")
EMAIL_PORT = retrieve_secret_configuration("EMAIL_PORT")

# TEMPLATE_DIRS += ("",)
# INSTALLED_APPS += ("",)

# Basic Logging Configuration
# https://docs.djangoproject.com/en/1.7/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename':'/home/ubuntu/RAPID/RAPID.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
