from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserLoginForm


def userRegistration(request):
    if request.user.username:
        return redirect(dashBoard)
    form = UserCreationForm()
    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            message = 'User : ' + username + ' registered successfully !'
    return render(request, 'sites/registration.html', {'form': form, 'msg': message})


def userLogIn(request):
    if request.user.username:
        return redirect(dashBoard)
    form = UserLoginForm()
    message = ''
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user is None:
                message = 'Invalid log in details !'
            else:
                login(request, user)
                request.session['college_city'] = 'Bangalore'
                request.session['college_address'] = 'BTM 2nd Stage'
                return redirect(dashBoard)
    return render(request, 'sites/login.html', {'form': form, 'msg': message})


def dashBoard(request):
    return render(request, 'sites/dashboard.html')


def userLogOut(request):
    logout(request)
    return redirect(dashBoard)
