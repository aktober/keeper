from .base import *
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

ROOT_DIR = BASE_DIR

# for Heroku
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

ALLOWED_HOSTS = ['.herokuapp.com']

db_from_env = dj_database_url.config(conn_max_age=None)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '../../notes/static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
