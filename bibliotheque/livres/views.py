from django.shortcuts import get_object_or_404, redirect, render

from livres.forms import LivreForm
from .models import Livre

def liste_livres(request):
    livres = Livre.objects.filter(disponible=True)
    return render(request, 'liste_livres.html', {'livres': livres})


# def detail_livre(request, livre_id):
#     livre = Livre.objects.get(id=livre_id)
#     return render(request, 'livres/detail_livre.html', {'livre': livre})


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
    livre = get_object_or_404(Livre, pk=livre_id)  # Récupère le livre à mettre à jour

    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)  # Lier le formulaire au livre existant
        if form.is_valid():
            form.save()  # Sauvegarde les modifications
            return redirect('liste_livres')  # Redirige vers la liste des livres
    else:
        form = LivreForm(instance=livre)  # Crée le formulaire avec les données existantes du livre

    return render(request, 'update_livre.html', {'form': form, 'livre': livre})

# Emprunter un livre
def emprunter_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    if livre.disponible:
        livre.disponible = False
        livre.save()
    return redirect('liste_livres')


def delete_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    
    # Si la méthode est POST, supprimer le livre
    if request.method == "POST":
        livre.delete()
        return redirect('livres:liste_livres')  # Redirige vers la liste des livres après suppression

    return render(request, 'livres:delete_livre.html', {'livre': livre})