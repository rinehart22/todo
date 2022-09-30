

from django.urls import path
from .import views
urlpatterns = [
    
    path('', views.home,  name='home'),
    path('create/', views.create, name='create'),
    path('read/<str:id>/', views.read, name="read"),
    path('delete/<str:id>/', views.delete, name="delete"),
    path('update/<str:id>/', views.update, name="update"),


]