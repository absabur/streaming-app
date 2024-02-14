from django.urls import path
from App_Auth.views import *

app_name = 'App_Auth'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
