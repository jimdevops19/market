from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def redirect_home(request):
    return redirect('home')

def homepage(request):
    return render(request, template_name='main/home.html')

@login_required(login_url='login')
def itemspage(request):
    if request.method =='POST':
        purchased_item = request.POST.get('purchased-item')
        purchased_item_object = Item.objects.get(name=purchased_item)
        if purchased_item_object:
            purchased_item_object.owner = request.user
            purchased_item_object.save()
            messages.success(request, f'Congratulations, You have bought {purchased_item_object.name} for {purchased_item_object.price}$ ')
            print(f'Congratulations! {request.user.username} has purchased {purchased_item_object.name}')
        return redirect('items')

    if request.method == 'GET':
        items = Item.objects.filter(owner=None)
        return render(request, template_name='main/items.html', context={'items':items})

def registerpage(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account has been created successfully, you are now logged in as {username}')
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return redirect('register')

    if request.method == 'GET':
        return render(request, template_name='main/register.html', context={'form': form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {username}')
            return redirect('items')
        else:
            messages.error(request, f'Username and Password combination is wrong! Please try again.')
            return redirect('login')

    if request.method == 'GET':
        return render(request, template_name='main/login.html')

def logoutpage(request):
    logout(request)
    messages.success(request, f'You are now logged out')
    return redirect('home')