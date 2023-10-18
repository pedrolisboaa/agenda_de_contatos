from django.urls import path
from .views import index, contato_unico, buscar

urlpatterns = [ 
    path('<int:id_contato>/', contato_unico, name='contato_unico'),
    path('buscar/', buscar, name='buscar'),
    path('', index, name='index'),
   
]