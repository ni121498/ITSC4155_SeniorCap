from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Module, Lesson, Cheatsheet, Block
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def index(request):
     modules_list = Module.objects.order_by('-module_number')[0:]
     context = {'modules_list': modules_list}
     return render(request, 'mainSite/index.html', context)
 
def module(request, title):
    module = get_object_or_404(Module, title = title)
    return render(request, 'mainSite/modules.html', {'module': module})
    #return render(request, 'mainSite/index.html', context)
    #return HttpResponse("You're looking at module %s." % module_id)

def lesson(request, title, lesson_title):
    lesson = get_object_or_404(Lesson, lesson_title = lesson_title)
    module = get_object_or_404(Module, title = title)
    return render(request, 'mainSite/lesson.html', {'lesson': lesson, 'module' : module})

def languages(request):
    modules_list = Module.objects.order_by('-module_number')[0:]
    context = {'modules_list': modules_list}
    return render(request, 'mainSite/languages.html', context)

def cheatsheet(request):
    cheatsheet_list = Cheatsheet.objects.order_by('-language')[0:]
    context = {'cheatsheet_list': cheatsheet_list}
    return render(request, 'mainSite/cheatsheet.html', context)

def cheatsheet_c(request, language):
    cheatsheet = get_object_or_404(Cheatsheet, language = language)
    cheatsheet_list = Cheatsheet.objects.order_by('-language')[0:]
    context = {'cheatsheet_list': cheatsheet_list, 'cheatsheet': cheatsheet}
    return render(request, 'mainSite/cheatsheet_c.html', context)

def cheatsheet_java(request):
    return render(request, template_name='mainSite/cheatsheet_java.html')

def cheatsheet_python(request):
        return render(request, template_name='mainSite/cheatsheet_python.html')

# def cheatsheet_java(request):
#     return render(request, template_name='mainSite/cheatsheet_java.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    
