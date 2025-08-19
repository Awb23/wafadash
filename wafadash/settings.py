# wafadash/settings.py

import os
from pathlib import Path

# --- BASE DIR ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY (Hardcoded - NOT RECOMMENDED) ---
# WARNING: This is insecure. Do not use this key in a real production app.
SECRET_KEY = 'django-insecure-0a*vm1x8dcuhrk6=hd7xj@4+*w-2jx45n+r8v*%!^mu+axbe_1'
DEBUG = False # Should always be False in production

# --- NETWORKING ---
# This is for the integrated setup where Django serves React
ALLOWED_HOSTS = [
    'wafadash-production.up.railway.app', # Your main Railway domain
    '127.0.0.1',
    'localhost',
]
CSRF_TRUSTED_ORIGINS = [
    'https://wafadash-production.up.railway.app',
    'web-production-7593.up.railway.app',
]
CORS_ALLOW_CREDENTIALS = True
# Since the frontend is served from the same domain, specific CORS origins are less critical
# but it's good practice to have for local development
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'web-production-7593.up.railway.app',
]

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

# --- DATABASE (Hardcoded - NOT RECOMMENDED FOR PRODUCTION) ---
# WARNING: This is insecure. Anyone with your code can access your database.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "mnLrZnYrQUwtsiLEyrDYOmFHYqTcTRYE",
        "HOST": "switchback.proxy.rlwy.net",  # دير host اللي عاطيك Railway
        "PORT": "32338",
    }
}

# --- AUTHENTICATION ---
AUTH_USER_MODEL = 'USERS.USER'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# --- STATIC FILES (Configured for WhiteNoise & React) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'front/dist'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- OTHER SETTINGS ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# In your settings.py file

ALLOWED_HOSTS = [
    '*',
]