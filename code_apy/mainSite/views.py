from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Module, Lesson
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def index(request):
     modules_list = Module.objects.order_by('-module_number')[0:]
     context = {'modules_list': modules_list}
     return render(request, 'mainSite/index.html', context)
 
def module(request,title):
    module = get_object_or_404(Module, title = title)
    return render(request, 'mainSite/modules.html', {'module': module})
    #return render(request, 'mainSite/index.html', context)
    #return HttpResponse("You're looking at module %s." % module_id)

def lesson(request, lesson_title):
    lesson = get_object_or_404(Lesson, lesson_title = lesson_title)
    return render(request, 'mainSite/lesson.html', {'lesson': lesson})

def languages(request):
    modules_list = Module.objects.order_by('-module_number')[0:]
    context = {'modules_list': modules_list}
    return render(request, 'mainSite/languages.html', context)

def cheatsheet(request):
    return render(request, template_name='mainSite/cheatsheet.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
