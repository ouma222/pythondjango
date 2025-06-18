from django.contrib import admin
from Feedy.models import Message

# Version 1 : Déclaration explicite
class MessageAdmin(admin.ModelAdmin):
    # Configuration personnalisée ici
    list_display = ('id', 'content', 'created_at')  # Exemple avec des champs typiques
    search_fields = ('content',)  # Champs utilisés pour la recherche
    list_filter = ('created_at',)  # Filtres disponibles

# Enregistrement du modèle avec sa classe Admin
admin.site.register(Message, MessageAdmin)