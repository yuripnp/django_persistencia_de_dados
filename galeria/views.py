from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-id')
    return render(request, 'galeria/index.html', {'fotografias': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})
