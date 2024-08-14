from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(label="Comment")

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    name = forms.CharField(label="Name")
    username = forms.CharField(label="Username")
    email = forms.CharField(label="E-Mail Address")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

