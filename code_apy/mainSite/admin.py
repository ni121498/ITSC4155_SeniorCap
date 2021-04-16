from django.contrib import admin, auth
from .models import Lesson, Module

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Module)