from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /home/5/
    path('languages/<str:title>/', views.module, name='detail'),
    # ex: /home/5/lesson/
    path('languages/<str:title>/str:lesson_title/', views.lesson, name='results'),

    path('languages/', views.languages, name='languages'),

    path('cheatsheet/', views.cheatsheet, name='cheatsheet'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]