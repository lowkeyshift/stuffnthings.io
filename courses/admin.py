from django.contrib import admin

from .models import Courses

# This is where you add your models you created
# This is so they can be viewed from the admin portal
admin.site.register(Courses)