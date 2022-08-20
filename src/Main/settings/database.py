# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


from Main.settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': DB_NAME,
#         'USER': DB_USER,
#         'PASSWORD': DB_PASS,
#         'HOST': DB_HOST,
#         'PORT': DB_PORT,
#     }
# }
