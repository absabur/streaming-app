from django.contrib import admin
from App_Videos.models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Likes)