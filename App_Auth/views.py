from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup_view(request):
    logout(request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!")
            return redirect('App_Auth:login')
    else:
        form = UserCreationForm()
    return render(request, 'App_Auth/signup.html', {'form': form})

def login_view(request):
    logout(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,"Login successful!")
            try:
                if request.GET['next']:
                    return redirect(request.GET['next'])
            except Exception as e:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'App_Auth/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request,"Logout successful!")
    return redirect('home')
