from django.contrib import admin
from .models import Livre, Emprunt

admin.site.register(Livre)
admin.site.register(Emprunt)

# @admin.register(Livre)
# class LivreAdmin(admin.ModelAdmin):
#     list_display = ('titre', 'auteur', 'disponible')
#     list_filter=('disponible',)


# @admin.register(Emprunt)
# class LivreAdmin(admin.ModelAdmin):
#     list_display = ('livre','non_emprunteur','date_emprunt')
