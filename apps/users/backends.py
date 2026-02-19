"""
Allow login by email or username. No restriction on duplicate emails at login
(if multiple users share an email, the first match is used).
"""
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None
        if '@' in username:
            user = User.objects.filter(email=username).first()
        else:
            user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            return user
        return None
