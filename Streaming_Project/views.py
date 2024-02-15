from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse

# View for the home page
def home(request):
    return HttpResponseRedirect(reverse('App_Videos:videos'))


# views.py
# from django.shortcuts import render
# def handler404(request, exception):
#     return redirect("home")
