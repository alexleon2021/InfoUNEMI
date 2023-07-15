from django.shortcuts import get_object_or_404, render
from .models import Bloque

# Create your views here.

def home(request):
    return render(request, 'home.html')

def bloque(request, bloque_id):
    bloque = get_object_or_404(Bloque, id=bloque_id)
    ##sitio = bloque.sitio.all()
    return render(request, 'bloque.html', {'curso': bloque})