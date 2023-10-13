from django.shortcuts import render, redirect
from .models import CustomUser
import logging

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = CustomUser.objects.get(username=username, password=password)
            return redirect('home')
        except CustomUser.DoesNotExist:
            return redirect('register') 
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        CustomUser.objects.create(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')



