from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, RoomRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import RoomRequest

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Неверный логин или пароль')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    requests = RoomRequest.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'requests': requests})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = RoomRequestForm(request.POST, request.FILES)
        if form.is_valid():
            room_request = form.save(commit=False)
            room_request.user = request.user
            room_request.save()
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect('dashboard')
    else:
        form = RoomRequestForm()
    return render(request, 'submit_request.html', {'form': form})
