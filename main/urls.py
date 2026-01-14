from django.urls import path
from . import views

urlpatterns = [
        path("index/", views.resident_data, name="resident")
        ]
