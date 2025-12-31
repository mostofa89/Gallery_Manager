from django.shortcuts import redirect, render
from django.contrib import messages as message
from django.contrib.auth import authenticate, login, logout
from user.models import User
from .forms import UserForm
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            message.success(request, 'Registration successful. You can now log in.')
            return redirect('user-login')
    else:
        form = UserForm()
    return render(request, 'user/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)
            if user:
               login(request, user)
               message.success(request, 'Login successful.')
               print("Login successful.")
               return redirect('gallery:gallery')
            
            else:
                message.error(request, 'Invalid username or password.')
                print("Invalid credentials.")

        except User.DoesNotExist:
            print("User does not exist.")
            message.error(request, 'Invalid username or password.')
            
    return render(request, 'user/login.html')


def logout_view(request):
    logout(request)
    message.success(request, 'You have been logged out.')
    return redirect('user:login')