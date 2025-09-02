from django.http import HttpResponse
from django.shortcuts import render
# def proy1(request):
#     return HttpResponse("<h1>Bienvenidos a mi pagina</h1>")
# def proy2(request):
#     return render(request, 'log.html')
def login(request):
    return render(request, './paginas/Login.html')

def calcularFactorial(request):
    resultado = None
    if request.method == 'POST':
        numero = request.POST.get('numero')
        if numero is not None and numero.isdigit():
            n = int(numero)
            resultado = 1
            for i in range(2, n + 1):
                resultado *= i
    print(resultado)
    return render(request, './paginas/factorial.html', {'resultado': resultado})

def datos(request):
    return render(request, './paginas/datos.html')
