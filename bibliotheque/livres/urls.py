from django.urls import path
from . import views
app_name='livres'
urlpatterns = [
    path('', views.liste_livres, name='liste_livres'),
    # path('livre/<int:livre_id>/', views.detail_livre, name='detail_livre'),
    path('livre/<int:livre_id>/delete/', views.delete_livre, name='delete_livre'),  # URL pour supprimer un livre

    path('livre/<int:livre_id>/update/', views.update_livre, name='update_livre'),  # Mise à jour du livre
    # path('livres_non_disponibles/', views.livres_non_disponibles, name='livres_non_disponibles'),
    path('livre/<int:livre_id>/emprunter/', views.emprunter_livre, name='emprunter_livre'),
    path('ajouter_livre/', views.ajouter_livre, name='ajouter_livre'),
]
