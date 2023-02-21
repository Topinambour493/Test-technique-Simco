# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "THE_MOST_SECRET_KEY_ISlkjnsdfljnslinvesoimsreljnrtblkjndbknljnergkjldfvjhbeviunerfiergiu4587y2h3r089uwev9jn98hf98jv3kjn"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "NAME": "pokedex",
        "USER": "simco",
        "PASSWORD": "password",
        "PORT": 5432,
    }
}
