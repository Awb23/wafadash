# wafadash/settings.py

import os
from pathlib import Path

# --- BASE DIR ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY (Hardcoded - NOT RECOMMENDED) ---
# WARNING: This is insecure. Do not use this key in a real production app.
SECRET_KEY = 'django-insecure-0a*vm1x8dcuhrk6=hd7xj@4+*w-2jx45n+r8v*%!^mu+axbe_1'
DEBUG = True # Should always be False in production

# --- NETWORKING ---
# Replace with your REAL frontend URL from Railway
FRONTEND_URL = "https://frontend-production-a459.up.railway.app" 

ALLOWED_HOSTS = [
    'wafadash-production.up.railway.app', # Your backend domain
    FRONTEND_URL.split('//')[1],      # Your frontend domain
    '127.0.0.1',
    'localhost',
    'https://wafadash-production-facb.up.railway.app'
]

CSRF_TRUSTED_ORIGINS = [
    f"https://{FRONTEND_URL.split('//')[1]}",
    "https://wafadash-production.up.railway.app",
    "https://wafadash-production-facb.up.railway.app"
]
CORS_ALLOWED_ORIGINS = [
    FRONTEND_URL,
    "http://localhost:5173",
    "https://wafadash-production-facb.up.railway.app"
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
    # WhiteNoise is removed as it's not needed for an API-only backend
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wafadash.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [], # Backend is an API, no extra template dirs needed
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
        "PASSWORD": "tNvjmBUZiXyykyrSDoeXuyviYZLVnnSU", # This is a secret
        "HOST": "turntable.proxy.rlwy.net",
        "PORT": "19200",
    }
}

# --- AUTHENTICATION ---
AUTH_USER_MODEL = 'USERS.USER'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# --- STATIC & MEDIA FILES ---
# For Django's admin panel
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- OTHER SETTINGS ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# In wafadash/settings.py

ALLOWED_HOSTS = [
    'wafadash-production-facb.up.railway.app', # <-- Add this new domain
    'wafadash-production.up.railway.app',     # Keep your old one too
    '127.0.0.1',
    'localhost',
]