from django.urls import path, include
from todoapp import views

urlpatterns = [
    path('', views.home, name='home_link'),
    path('data', views.formdata, name='database_link'),
]