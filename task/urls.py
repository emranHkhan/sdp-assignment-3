from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='task.show'),
    path('add/', views.add, name='task.add'),
    path('edit/<int:id>', views.edit, name='task.edit'),
    path('delete/<int:id>', views.delete, name='task.delete')
]
