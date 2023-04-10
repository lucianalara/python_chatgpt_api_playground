from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('chat/', views.chat_api, name='python_chatgpt_api_playground'),
]
