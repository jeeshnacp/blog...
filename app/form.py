from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import user, Login


class loginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)



class userregister(forms.ModelForm):
    class Meta:
        model=user
        fields=('name','address','contact_no','email')

