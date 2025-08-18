# wafadash/settings.py
import os
from pathlib import Path

# -------------------------------------------------
# BASE DIR
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------
# SECURITY
# -------------------------------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-0a*vm1x8dcuhrk6=hd7xj@4+*w-2jx45n+r8v*%!^mu+axbe_1",  # fallback (local)
)

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
  "*"
        # ✅ زيد هاد الدومين
]

# Add Railway hostname automatically if available
RAILWAY_HOSTNAME = os.environ.get("RAILWAY_HOSTNAME")
if RAILWAY_HOSTNAME:
    ALLOWED_HOSTS.append(f".{RAILWAY_HOSTNAME}")

# -------------------------------------------------
# CORS / CSRF
# -------------------------------------------------
CSRF_TRUSTED_ORIGINS = [
    "https://wafadash-production.up.railway.app",
    "https://frontend-production-a459.up.railway.app",  # frontend 1
    "https://web-production-4c372.up.railway.app", 
         "https://wafadash-production-a087.up.railway.app/",
            "wafadash-production-a087.up.railway.app",  # frontend 2
]
DEBUG=True

CORS_ALLOWED_ORIGINS = [
    "https://frontend-production-a459.up.railway.app",
    "https://web-production-4c372.up.railway.app",
    "http://localhost:5173",
      "wafadash-production-a087.up.railway.app"  # for local React dev
]

CORS_ALLOW_CREDENTIALS = True

# -------------------------------------------------
# APPLICATIONS
# -------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    # Local apps
    "USERS",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "wafadash.urls"

# -------------------------------------------------
# TEMPLATES (React frontend)
# -------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
         "DIRS": [BASE_DIR / "front" / "dist"],  

        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wafadash.wsgi.application"

# -------------------------------------------------
# DATABASE (Postgres via Railway)
# -------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "tNvjmBUZiXyykyrSDoeXuyviYZLVnnSU",
        "HOST": "turntable.proxy.rlwy.net",
        "PORT": "19200",
    }
}

# -------------------------------------------------
# AUTH & DRF
# -------------------------------------------------
AUTH_USER_MODEL = "USERS.USER"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

# -------------------------------------------------
# I18N / TIMEZONE
# -------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -------------------------------------------------
# STATIC FILES
# 
# --- NETWORKING SETTINGS ---
# This list is now clean and uses the correct syntax.

]
# Add the auto-generated Railway URL if it exists
RAILWAY_STATIC_URL = os.environ.get('RAILWAY_STATIC_URL')
if RAILWAY_STATIC_URL:
    ALLOWED_HOSTS.append(RAILWAY_STATIC_URL.split('//')[1]) # Add without https://

CSRF_TRUSTED_ORIGINS = [
    'https://wafadash-production.up.railway.app',
    'https://frontend-production-a459.up.railway.app',
    'https://web-production-4c372.up.railway.app',
    'https://wafadash-production-a087.up.railway.app/',
]
CORS_ALLOWED_ORIGINS = [
    'https://frontend-production-a459.up.railway.app',
    'https://web-production-4c372.up.railway.app',
    'https://wafadash-production-a087.up.railway.app/',
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