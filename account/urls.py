from django.urls import path
from account import views
urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
]
