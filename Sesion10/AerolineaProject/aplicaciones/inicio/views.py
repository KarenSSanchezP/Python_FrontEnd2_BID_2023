from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'inicio/index.html')

def consultar_precios(request):
    pagina = 1

    if request.GET:
        pagina = int(request.GET['page'])
    
    url_binance = 'https://api.binance.com/api/v3/ticker/price'
    datos = requests.get(url_binance)

    contexto = {'precios': datos.json()[pagina*10-10:pagina*10:]}
    return render(request, 'inicio/consultar-precios.html', contexto)

def consultar_precios_js(request):
    return render(request, 'inicio/consultar-precios-js.html')


def ejercicio1_api(request):
    url_users = 'https://jsonplaceholder.typicode.com/users'
    datos = requests.get(url_users)

    contexto = {'usuarios': datos.json()}
    return render(request, 'inicio/ejercicio1-api.html', contexto)
