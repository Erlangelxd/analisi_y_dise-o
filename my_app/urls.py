from django.urls import path
from my_app import views
urlpatterns = [
    path("login/", views.login, name="login"),
    # path("conv/", views.proy2, name="proyecto2"),
    path("fact/", views.calcularFactorial, name="factorial"),
    path("fibo/", views.serie_fibonacci, name="fibonacci"),
    path("datos/", views.datos, name="log"),
    path("primo/", views.primo, name="primo"),
    path("calculadora/", views.calcular_masa_corporal, name="calculadora"),
]
