from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),  # Corrigé 'details' en 'detail' pour matcher votre vue
    path('message/<int:id>/', views.detail, name='message_detail'),
]