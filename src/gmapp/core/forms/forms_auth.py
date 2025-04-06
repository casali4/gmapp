from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


#...

class CustomLoginForm(forms.Form):

    username = forms.CharField(

        max_length=150,

        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),

        label='username'

    )

    password = forms.CharField(

        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}),

        label='password'

    )

  

class OwnUserCreationForm(UserCreationForm):

  class Meta:

    model = User

    fields = ['username', 'password1', 'password2', 'email'] 

  

  def __init__(self, *args, **kwargs):

    super().__init__(*args, **kwargs)

    self.fields['username'].widget.attrs.update({'class': 'form-control'})

    self.fields['username'].label = 'Benutzername'

    self.fields['password1'].widget.attrs.update({'class': 'form-control'})

    self.fields['password1'].label = 'Passwort'

    self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    self.fields['password2'].label = 'Passwort wiederholen'

    self.fields['email'].widget.attrs.update({'class': 'form-control'})

    self.fields['email'].label = 'E-Mail'

  

    if 'usable_password' in self.fields:

      del self.fields['usable_password']