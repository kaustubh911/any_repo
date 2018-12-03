from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
