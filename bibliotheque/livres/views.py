from django.shortcuts import get_object_or_404, redirect, render
from .forms import LivreForm
from .models import Livre


def liste_livres(request):
    livres = Livre.objects.filter(disponible=True)
    return render(request, 'liste_livres.html', {'livres': livres})


def ajouter_livre(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livres:liste_livres')
    else:
        form = LivreForm()
    return render(request, 'ajouter_livre.html', {'form': form})


def update_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)

    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('livres:liste_livres')
    else:
        form = LivreForm(instance=livre)

    return render(request, 'update_livre.html', {'form': form, 'livre': livre})


def emprunter_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    if livre.disponible:
        livre.disponible = False
        livre.save()
    return redirect('livres:liste_livres')


def delete_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    
    if request.method == "POST":
        livre.delete()
        return redirect('livres:liste_livres')

    return render(request, 'delete_livre.html', {'livre': livre})
