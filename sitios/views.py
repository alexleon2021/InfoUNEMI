from django.shortcuts import get_object_or_404, render
from .models import Bloque
# Create your views here.

def home(request):
    bloques = Bloque.objects.all()
    return render(request, 'home.html', {'bloques': bloques})

def bloque(request, bloque_id):
    bloque = get_object_or_404(Bloque, id=bloque_id)
    sitios = bloque.sitio_set.all()
    return render(request, 'bloque.html', {'bloque': bloque, 'sitios': sitios })

def listadoBloques(request):
    bloques = Bloque.objects.all()
    return render(request, 'listadoBloques.html', {'bloques': bloques})

