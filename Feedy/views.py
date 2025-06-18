from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ruamel.yaml import comments

from Feedy.models import Message
from django.utils import timezone
from .models import Message, Comment  # Import des modèles
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse


@login_required  # S'assurer que l'utilisateur est connecté
def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:  # Vérifier que le contenu n'est pas vide
            Message.objects.create(
                content=content,
                user=request.user,  # Utiliser request.user directement
                created_at=timezone.now()  # Ajouter un timestamp
            )
            return redirect('index')  # Rediriger pour éviter les re-soumissions

    messages = Message.objects.order_by('-created_at')
    return render(request, "index.html", {'messages': messages})


def detail(request, id):
    context = {}  # Correction: ajout du signe = manquant
    message = Message.objects.get(id=id)  # Récupération du message unique
    context['message'] = message  # Ajout au contexte sous forme d'objet unique
    context['comments'] = comments
    print(id)  # Pour le débogage (à supprimer en production)
    return render(request, 'Feedy/index.html')
