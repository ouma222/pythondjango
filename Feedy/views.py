from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        "messages": [
            {
                "content": "Hello world!",
                "username": "CommentCoder",
                "created_at": datetime.now()
            },
            {
                "content": "Bienvenue sur le site.",
                "username": "DevTunisien",
                "created_at": datetime.now()
            },
            {
                "content": "Ceci est un message de test.",
                "username": "Admin",
                "created_at": datetime.now()
            },
        ]
    }
    return render(request, "index.html", context)
