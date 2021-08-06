from django.urls import path
from rest_framework import views
from .views import ListTodo, DetailTodo, LoginAPI, RegisterAPI
from knox import views as KnoxViews

urlpatterns = [
    path('auth/register', RegisterAPI.as_view(), name='register'),
    path('auth/login', LoginAPI.as_view(), name='Login'),
    path('auth/logout', KnoxViews.LogoutView.as_view(), name='logout'),
    path('', ListTodo.as_view(), name='list todo'),
    path('<int:pk>/', DetailTodo.as_view(), name='detail todo'),
]