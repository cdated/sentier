from __future__ import annotations

import os
from typing import Any

SECRET_KEY = "DEV_SECURITY_KEY"

DEBUG = True

ALLOWED_HOSTS: list[str] = ["127.0.0.1", "10.0.1.24", "localhost", "10.0.1.4"]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Application definition

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = "sentier.wsgi.application"
