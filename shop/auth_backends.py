# auth_backends.py

from django.contrib.auth.backends import BaseBackend
from .models import Logins

class LoginModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Logins.objects.get(username=username)
            if user.password == password:  # You should ideally hash the password before storing and compare hashed passwords here
                return user
        except Logins.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return Logins.objects.get(pk=user_id)
        except Logins.DoesNotExist:
            return None
