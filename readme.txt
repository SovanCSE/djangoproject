#Install Django
>> pip install django

#check verion of django
>> django-admin --version
>> python -m django --version

#Create django project
>> django-admin startproject django_webapplication

#Create app in django application(chnage into outer directory(django_webapplication) which is
called as root directory of the project)

>> python manage.py startapp firstapp


#Run server from outer project directory:
>> python manage.py runserver

#For migrations
>> python manage.py makemigrations firstapp
>> python manage.py migrate firstapp

#command to create dajngo super user through commandline:
>> python manage.py createsuperuser

#command to see migration file details as sql format:
>> python manage.py sqlmigrate blog(app_name) 0001(first 4 digits from migration filename)

#to open django manage shell
>> python manage.py shell

#template folder setting
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

#static folder setting
STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static")]

#mysql configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'databasename',                      # Or path to database file if using sqlite3.
        'USER': 'username',                      # Not used with sqlite3.
        'PASSWORD':'password',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',
    }
}

Aws console to get credentials:
link: https://console.clever-cloud.com/users/me/addons/addon_4ca1ad55-9a7a-4235-9a70-f10c32324d93

#Database credential:
Host: bwvhetueagevuol4dyow-mysql.services.clever-cloud.com
Username: uugrmk7ezbk7lbec
Password: Mk9hhNQBcqlN2lImYTIY
database: bwvhetueagevuol4dyow
port: 3306

