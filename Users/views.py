from django.shortcuts import render, redirect  
from django.contrib.auth import login  
from .forms import UserRegisterForm  

def register(request):  
    if request.method == "POST":  
        form = UserRegisterForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            login(request, user)  
            return redirect('home')  
    else:  
        form = UserRegisterForm()  
    return render(request, 'Users/register.html', {'form': form})  

def home(request):
    return render(request, 'Users/home.html')
