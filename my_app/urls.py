from django.urls import path
from my_app import views
urlpatterns = [
    path("login/", views.login, name="login"),
    # path("conv/", views.proy2, name="proyecto2"),
    path("fact/", views.calcularFactorial, name="factorial"),
    path("datos/", views.datos, name="log"),
]
