from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# View for the home page
def home(request):
    return HttpResponseRedirect(reverse('App_Videos:videos'))


# views.py
from django.shortcuts import render
def handler404(request, exception):
    return render(request, '404.html', status=404)
