from django.urls import path
from App_Videos.views import *

app_name = 'App_Videos'

urlpatterns = [
    path('videos/', videos , name='videos'),
    path('video/<pk>/', video_details , name='video_details'),
    path('like/<pk>/', like , name='like'),
]
