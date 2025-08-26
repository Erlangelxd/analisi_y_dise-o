from django.urls import path
from .import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("p2/", views.proy2, name="proyecto 2"),
]
