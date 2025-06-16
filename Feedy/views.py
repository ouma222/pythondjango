from django.shortcuts import render
from datetime import datetime  # Il faut importer datetime si tu veux l'utiliser

# Create your views here.
def index(request):
    context = {
        "messages": [
            {
                "content": "text",
                "username": "CommentCoder",
                "created_at": datetime.now()
            }
        ]
    }
    return render(request,"index.html", context)
