"""
Django settings for PatientPro project.
"""

import os
from pathlib import Path

# =========================
# BASE DIRECTORY
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY
# =========================

SECRET_KEY = 'django-insecure-%7=t%2)%ag$j-b$k!1nj%@tc5ttdu4ov*^r*&uzbpxxts_pzn@'

# Change to False before deployment
DEBUG = True

ALLOWED_HOSTS = ['*']


# =========================
# INSTALLED APPS
# =========================

INSTALLED_APPS = [

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Allauth
    'allauth',
    'allauth.account',

    # DRF
    'rest_framework',

    # CORS
    'corsheaders',

    # Widgets
    'widget_tweaks',

    # Your app
    'MediAccess',
]


# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [

    # CORS
    'corsheaders.middleware.CorsMiddleware',

    # Security
    'django.middleware.security.SecurityMiddleware',

    # Whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Django middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Allauth
    'allauth.account.middleware.AccountMiddleware',
]


# =========================
# URLS / WSGI
# =========================

ROOT_URLCONF = 'PatientPro.urls'

WSGI_APPLICATION = 'PatientPro.wsgi.application'


# =========================
# TEMPLATES
# =========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],

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


# =========================
# DATABASE
# =========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# PASSWORD VALIDATION
# =========================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =========================
# INTERNATIONALIZATION
# =========================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# =========================
# STATIC FILES
# =========================

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)


# =========================
# DEFAULT PRIMARY KEY
# =========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================
# CUSTOM USER MODEL
# =========================

AUTH_USER_MODEL = 'MediAccess.CustomUser'


# =========================
# AUTHENTICATION BACKENDS
# =========================

AUTHENTICATION_BACKENDS = (

    # Django admin login
    'django.contrib.auth.backends.ModelBackend',

    # Django allauth
    'allauth.account.auth_backends.AuthenticationBackend',
)


# =========================
# LOGIN / LOGOUT
# =========================

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'user_type_choice'

LOGOUT_REDIRECT_URL = 'login'


# =========================
# DRF CONFIGURATION
# =========================

REST_FRAMEWORK = {

    # JWT Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # Default permissions
    'DEFAULT_PERMISSION_CLASSES': (

        'rest_framework.permissions.IsAuthenticated',
    ),
}


# =========================
# CORS CONFIGURATION
# =========================

# Allow frontend connection later
CORS_ALLOW_ALL_ORIGINS = True