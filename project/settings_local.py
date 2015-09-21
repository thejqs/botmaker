#First thing: Make sure to add this file to your .gitignore 
# so you don't accidentally make it public

# go get a secret key from, say, http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'PUT IT IN THIS STRING'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NAME OF YOUR DATABASE',
        'HOST': '127.0.0.1',
        'USER': 'YOUR USER',
        'PASSWORD': 'YOUR DB PASSWORD',
        'PORT': '',
    }
}

# email settings for gmail, which you might not need. But if you do:
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'YOUR EMAIL@gmail.com'
EMAIL_HOST_PASSWORD = 'YOUR PASSWORD'
EMAIL_USE_TLS = True

# When you register your app with Twitter, you'll need these. 
# Best to make sure they're not public.
# Get them from apps.twitter.com when you create your bot account.
auth_settings = {
    'consumer_key': 'BUNCH OF GIBBERISH',
    'consumer_secret': 'BUNCH OF GIBBERISH',
    'access_token_key': 'BUNCH OF GIBBERISH',
    'access_token_secret': 'BUNCH OF GIBBERISH'
}
