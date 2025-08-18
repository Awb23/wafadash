

# wafadash/settings.py

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY SETTINGS (Loaded from Environment Variables) ---
# IMPORTANT: You MUST set these variables in the Railway "Variables" tab
SECRET_KEY = os.environ.get('SECRET_KEY')
# DEBUG is False by default on Railway unless you set it to 'True'
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
SECRET_KEY = 'django-insecure-0a*vm1x8dcuhrk6=hd7xj@4+*w-2jx45n+r8v*%!^mu+axbe_1'
# --- NETWORKING SETTINGS ---
# --- NETWORKING SETTINGS ---
ALLOWED_HOSTS = [
    'wafadash-production.up.railway.app', # Your Railway domain
    '127.0.0.1',
    'localhost',
    'https://web-production-4c372.up.railway.app/'
]
# Add the auto-generated Railway URL if it exists
RAILWAY_STATIC_URL = os.environ.get('RAILWAY_STATIC_URL')
if RAILWAY_STATIC_URL:
    ALLOWED_HOSTS.append(RAILWAY_STATIC_URL)

CSRF_TRUSTED_ORIGINS = [
    'https://wafadash-production.up.railway.app',
    'https://web-production-4c372.up.railway.app',
]
CORS_ALLOWED_ORIGINS = [
    'https://wafadash-production.up.railway.app',

    'https://web-production-4c372.up.railway.app',

    'http://localhost:5173', # For local development
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
    # Third-party apps
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    # Your app
    'USERS',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise Middleware - MUST be right after SecurityMiddleware
   
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
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # This tells Django to look for index.html in your React build folder
        'DIRS': [os.path.join(BASE_DIR, 'front/dist')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wafadash.wsgi.application'

# --- DATABASE (Configured for Railway) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'tNvjmBUZiXyykyrSDoeXuyviYZLVnnSU',
        'HOST': 'turntable.proxy.rlwy.net',
        'PORT': '19200',
    }
}


# --- AUTHENTICATION ---
AUTH_USER_MODEL = 'USERS.USER'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES (Configured for WhiteNoise & React) ---


# --- Default primary key field type ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'