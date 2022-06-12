
from django.shortcuts import render,redirect
from .forms import  UserRegistrationForm
# Create your views here.
def register(response):
    
    if response.method == 'POST':
        form = UserRegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            redirect('/home')
    else:
        form = UserRegistrationForm()

    form = UserRegistrationForm()
    return render(response,"register.html",{"form":form})