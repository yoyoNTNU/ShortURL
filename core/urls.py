from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("private/", views.private_page),
    path("terms/", views.terms_of_service),
]