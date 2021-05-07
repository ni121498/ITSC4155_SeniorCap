from django.contrib import admin, auth
from .models import Lesson, Module, Cheatsheet, Block

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
        ('Language', {'fields' : ['language']})
    ]
    inlines = [LessonInline]


class BlockInline(admin.StackedInline):
    model = Block
    extra = 0


class CheatsheetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Cheatsheet Language', {'fields': ['language']}),
    ]
    inlines = [BlockInline]

admin.site.register(Module, ModuleAdmin)
admin.site.register(Lesson)
admin.site.register(Cheatsheet, CheatsheetAdmin)
admin.site.register(Block)