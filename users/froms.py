from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'username', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }

    



