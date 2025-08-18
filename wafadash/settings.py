# wafadash/settings.py

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY SETTINGS ---
# IMPORTANT: Your SECRET_KEY is kept here for now, but for real production,
# you should move it to Railway's "Variables" tab and use os.environ.get('SECRET_KEY')
SECRET_KEY = 'django-insecure-0a*vm1x8dcuhrk6=hd7xj@4+*w-2jx45n+r8v*%!^mu+axbe_1'

# DEBUG should be False in production. It's safer to control this with a Railway variable.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# --- NETWORKING SETTINGS ---
# This list is now clean and uses the correct syntax.
ALLOWED_HOSTS = [
    'wafadash-production.up.railway.app',
    'frontend-production-a459.up.railway.app', # Your frontend URL
    'web-production-4c372.up.railway.app', # Another frontend URL you used
    '127.0.0.1',
    'localhost',
]
# Add the auto-generated Railway URL if it exists
RAILWAY_STATIC_URL = os.environ.get('RAILWAY_STATIC_URL')
if RAILWAY_STATIC_URL:
    ALLOWED_HOSTS.append(RAILWAY_STATIC_URL.split('//')[1]) # Add without https://

CSRF_TRUSTED_ORIGINS = [
    'https://wafadash-production.up.railway.app',
    'https://frontend-production-a459.up.railway.app',
    'https://web-production-4c372.up.railway.app',
]
CORS_ALLOWED_ORIGINS = [
    'https://frontend-production-a459.up.railway.app',
    'https://web-production-4c372.up.railway.app',
    'http://localhost:5173',
]
CORS_ALLOW_CREDENTIALS = True

# --- APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'USERS',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # For serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wafadash.urls'

# --- TEMPLATES (Configured for React) ---
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'front/dist')], # Path to React's index.html
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'wafadash.wsgi.application'

# --- DATABASE (Configured for Railway) ---
# This will use the DATABASE_URL from Railway's environment variables.
# For local development, it will fall back to a local sqlite3 database.
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=False # Set to False to work with both local and Railway
    )
}

# --- AUTHENTICATION & REST FRAMEWORK ---
AUTH_USER_MODEL = 'USERS.USER'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES (Configured for WhiteNoise & React) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'front/dist'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Default primary key field type ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'