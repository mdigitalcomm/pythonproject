from django.urls import path
from appone import views

urlpatterns = [
    path('', views.index, name="appone-index"),
]