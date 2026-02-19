import re
import random
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterForm(forms.Form):
    """Register with email and password only. Username is auto-generated (no uniqueness errors)."""
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='At least 8 characters; not too similar to your email; not commonly used.',
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            validate_password(password1)
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def _generate_username(self, email):
        base = re.sub(r'[^\w.]', '', email.split('@')[0])[:100] or 'user'
        username = base
        while User.objects.filter(username=username).exists():
            username = f"{base}_{random.randint(1000, 9999)}"
        return username

    def save(self, commit=True):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        username = self._generate_username(email)
        user = User.objects.create_user(username=username, email=email, password=password)
        return user
