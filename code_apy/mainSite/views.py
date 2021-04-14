from django.shortcuts import render

from django.http import HttpResponse
from .models import Module


def index(request):
     modules_list = Module.objects.order_by('-module_number')[0:]
     context = {'modules_list': modules_list}
     return render(request, 'mainSite/index.html', context)
 
def module(request,module_id):
    return HttpResponse("You're looking at module %s." % module_id)

def lesson(request, lesson_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
