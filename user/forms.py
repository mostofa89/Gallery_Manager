from django import forms
from .models import User
from django.contrib.auth.hashers import make_password

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-3 py-3 border rounded-lg focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-3 border rounded-lg focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Email'
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'w-full px-3 py-3 border rounded-lg focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Password'
            }),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

