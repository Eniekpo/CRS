from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignupForm
from . models import Record

# Create your views here.


def records(request):
    records = Record.objects.all()
    return render(request, 'App/records.html', {'records': records})


def index(request):
    return render(request, 'App/index.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged in")
            return redirect('index')
        else:
            messages.success(request, "Error in username or password")
            return redirect('login')
    else:
        return render(request, 'App/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Loggeed Out")
    return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You Have Successfully Registered! Welcome")
            return redirect('index')
    else:
        form = SignupForm()
        return render(request, 'App/register.html', {'form': form})

    return render(request, 'App/register.html', {'form': form})
