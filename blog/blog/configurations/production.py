from.base import *
 
# TODO: dejar solo el dominio de prod
ALLOWED_HOSTS= ['localhost', '127.0.0.1', 'mi-dominio-prod-ejemplo.com']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: cambiar la config de la base de datos para prod
DATABASES = {
    'default': {

        #'ENGINE': 'django.db.backends.postgresql',
        
        # En caso de usar mysql
        'ENGINE': 'django.db.backends.mysql',

        "NAME":os.getenv('DB_NAME'),
        "USER":os.getenv('DB_USER'),
        "PASSWORD":os.getenv('DB_PASSWORD'),
        "HOST":os.getenv('DB_HOST'),
        "PORT":os.getenv('DB_PORT'),
   }
}

os.environ['DJANGO_PORT'] ='8080'