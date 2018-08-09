from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # The user is sending his info for signup
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                if user:
                    return render(request, 'accounts/signup.html', \
                    {'error': 'Username %s has already been taken!'%request.POST['username']})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],\
                password = request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', \
            {'error': 'Passwords dont match!'})

    else:
        # User wants to come to the signup page
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        # user is giving his login info
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or Password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def accounts(request):
    return render(request, 'accounts/accounts.html')
