import os
from dotenv import load_dotenv

load_dotenv()
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django.contrib import messages
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4p3z#vs%7b1(39$$$qzdrpr%l_pfl-eo%3q*zj9lqj0hlympe-"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


# test4
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "para", # 코드 블럭 아래 이미지 참고하여 입력
#         "USER": "postgres",
#         "PASSWORD": "team8para!", # 데이터베이스 생성 시 작성한 패스워드
#         "HOST": "Para-env.eba-ezj4wh6p.ap-northeast-2.elasticbeanstalk.com", # 코드 블럭 아래 이미지 참고하여 입력
#         "PORT": "5432",
#     }
# }
DEBUG = os.getenv("DEBUG") == "True"
if DEBUG:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),  # 코드 블럭 아래 이미지 참고하여 입력
            "USER": "postgres",
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),  # 데이터베이스 생성 시 작성한 패스워드
            "HOST": os.getenv("DATABASE_HOST"),  # 코드 블럭 아래 이미지 참고하여 입력
            "PORT": "5432",
        }
    }


ALLOWED_HOSTS = [
    # "Elastic Beanstalk URL",
    "para-env.eba-ezj4wh6p.ap-northeast-2.elasticbeanstalk.com",  # 예시입니다. 본인 URL로 해주세요.
    "127.0.0.1",
    "localhost",
]


# Application definition

INSTALLED_APPS = [
    "storages",  # storages 추가
    "channels",
    "daphne",
    "chat",
    "django_private_chat2.apps.DjangoPrivateChat2Config",
    "accounts",
    "products",
    "reviews",
    "imagekit",
    "cart",
    "taggit.apps.TaggitAppConfig",
    "taggit_templatetags2",
    "django_extensions",
    "django_bootstrap5",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Allauth를 위한 Apps
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # ... 소셜로그인을 할 제공자 리스트를 아래에 포함
    # 네이버
    "allauth.socialaccount.providers.naver",
    # 카카오
    "allauth.socialaccount.providers.kakao",
]

TAGGIT_CASE_INSENSITIVE = True
TAGGIT_LIMIT = 50

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "libraries": {  # <----- add this
                "filter_tags": "config.filters",  # switch with your app name
                "custom_tags": "config.templatetags.custom_tags",
            },
        },
    },
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#         "TEST": {"NAME": BASE_DIR / "db_test.sqlite3"},
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

ADMIN_MEDIA_PREFIX = "/static/admin/"

# MEDIA_ROOT = BASE_DIR / "images"
# MEDIA_URL = "/media/"


# 아래 코드 추가
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

# AWS_REGION = "ap-northeast-2"
# AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
#     AWS_STORAGE_BUCKET_NAME,
#     AWS_REGION,
# )


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"

# 메세지 색상 변경
MESSAGE_TAGS = {
    messages.ERROR: "danger",
    messages.SUCCESS: "success",
}

# 이메일 회원가입 설정
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_FROM = "unboxing96@gmail.com"  # 발신 주소
EMAIL_HOST_USER = "unboxing96@gmail.com"  # 호스트 주소
EMAIL_HOST_PASSWORD = "ybsdoqbipsazoaqn"  # google에서 발급받은, 이메일 보내기 서비스를 이용하기 위한 2차 비밀번호
EMAIL_PORT = 587
EMAIL_USE_TLS = True
PASSWORD_RESET_TIMEOUT = 14400  # 인증용 메일 만료 시간(초) (4시간)

# Channels
ASGI_APPLICATION = "config.example.routing.application"

CHANNEL_LAYERS = {
    "default": {"BACKEND": "channels.layers.InMemoryChannelLayer"},
}

CART_SESSION_ID = "cart_item"
ACCOUNT_SESSION_REMEMBER = True

PRICES = (
    ("vi", "₫"),
    ("en", "$"),
)

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "loggers": {
#         "django.db.backends": {
#             "level": "DEBUG",
#             "handlers": ["console"],
#         }
#     },
# }
