from django.contrib import admin, auth
from .models import Lesson, Module

# Register your models here.
# admin.site.register(Lesson)
# admin.site.register(Module)

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0


class ModuleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Module Number', {'fields': ['module_number']}),
    ]
    inlines = [LessonInline]

admin.site.register(Module, ModuleAdmin)
admin.site.register(Lesson)