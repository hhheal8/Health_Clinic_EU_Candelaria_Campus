from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EucUsers

# Register your models here.
admin.site.register(EucUsers, UserAdmin)
