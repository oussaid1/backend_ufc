from os import link
from django.contrib import admin
from .models import users,User

# Register your models here.
admin.site.register(users)
admin.site.register(User)