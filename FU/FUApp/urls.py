from django.urls import path
from FUApp import views

urlpatterns = [
    path("", views.index, name='form_link'),
    path("data", views.form_data, name='form_data_display_link'),
]