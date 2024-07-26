from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm, UserUpdateForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            first_name = user.first_name
            last_name = user.last_name
            messages.success(request, f'Welcome back, {first_name} {last_name}!')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'authenticate/login_user.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful")
                return redirect('login_user')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login_user')

def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('settings')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'settings.html', {'form': form})
