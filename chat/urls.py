from django.urls import path
from .views import indexView, SalaView

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('chat/<str:nome_sala>/', SalaView.as_view(), name='sala'),
]