from django import forms
from bug_app.models import MyUser, Ticket


class TicketForm(forms.Form):
    title = forms.CharField(max_length=240)
    description = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput) 

class SignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)  