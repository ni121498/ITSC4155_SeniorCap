from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /languages/title/
    path('languages/', views.languages, name='languages'),
    path('languages/<str:title>/', views.module, name='module'),
    # ex: /languages/title/lesson_title/
    path('languages/<str:title>/<str:lesson_title>/', views.lesson, name='lesson'),
    path('cheatsheet/', views.cheatsheet, name='cheatsheet'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]