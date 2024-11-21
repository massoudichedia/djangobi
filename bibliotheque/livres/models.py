from django.db import models
from django.shortcuts import redirect, render

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200)
    date_publication = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titre} par {self.auteur}"

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    nom_emprunteur = models.CharField(max_length=200)
    date_emprunt = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_emprunteur} a emprunté {self.livre.titre}"

def update_livre(request, livre_id):
    livre = Livre.objects.get(id=livre_id)
    if request.method == "POST":
        livre.titre = request.POST['titre']
        livre.auteur = request.POST['auteur']
        livre.date_publication = request.POST['date_publication']
        livre.save()
        return redirect('livres:detail', livre_id=livre.id)
    return render(request, 'livres/update_livre.html', {'livre': livre})

def livres_non_disponibles(request):
    livres = Livre.objects.filter(disponible=False)
    return render(request, 'livres/livres_non_disponibles.html', {'livres': livres})

def emprunter_livre(request, livre_id):
    livre = Livre.objects.get(id=livre_id)
    if livre.disponible:
        livre.disponible = False
        livre.save()
        Emprunt.objects.create(livre=livre, nom_emprunteur=request.POST['nom_emprunteur'])
    return redirect('livres:liste')
