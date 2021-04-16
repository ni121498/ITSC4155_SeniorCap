from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /home/5/
    path('<int:module_id>/', views.module, name='detail'),
    # ex: /home/5/lesson/
    path('<int:module_id>/int:lesson_id/', views.lesson, name='results'),

    path('languages/', views.languages, name='languages'),

    path('cheatsheet/', views.cheatsheet, name='cheatsheet'),
]