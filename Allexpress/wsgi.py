"""
WSGI config for Allexpress project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Allexpress.settings')

application = get_wsgi_application()

# Automatic Superuser Creation
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get('SUPERUSER_USERNAME')
email = os.environ.get('SUPERUSER_EMAIL')
password = os.environ.get('SUPERUSER_PASSWORD')

if username and password and email:
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser {username}...")
        User.objects.create_superuser(
            username=username, 
            email=email, 
            password=password,
            first_name="Admin",
            last_name="User"
        )
    else:
        print(f"Superuser {username} already exists.")


