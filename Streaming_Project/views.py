from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# View for the home page
def home(request):
    return HttpResponseRedirect(reverse('App_Videos:videos'))
