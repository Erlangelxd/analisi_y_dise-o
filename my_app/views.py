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

def serie_fibonacci(request):
    serie = None
    if request.method == 'POST':
        numero = request.POST.get('numero')
        if numero is not None and numero.isdigit():
            n = int(numero)
            serie = []
            a, b = 0, 1
            for _ in range(n):
                serie.append(a)
                a, b = b, a + b
    return render(request, './paginas/serie.html', {'serie': serie})

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primo(request):
    resultado = None
    if request.method == 'POST':
        numero = request.POST.get('numero')
        if numero is not None and numero.isdigit():
            n = int(numero)
            resultado = "Es primo" if es_primo(n) else "No es primo"
    return render(request, './paginas/primo.html', {'resultado': resultado})

def datos(request):
    return render(request, './paginas/datos.html')
