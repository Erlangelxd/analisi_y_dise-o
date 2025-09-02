from django.http import HttpResponse
from django.shortcuts import render
# def proy1(request):
#     return HttpResponse("<h1>Bienvenidos a mi pagina</h1>")
# def proy2(request):
#     return render(request, 'log.html')
def login(request):
    return render(request, 'Login.html')
def calcularFactorial(request):
    return render(request, 'factorial.html')
def datos(request):
    return render(request, 'datos.html')