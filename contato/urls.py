from django.urls import path
from .views import index, contato_unico, buscar, criar, atualizar, deletar

urlpatterns = [ 
    path('buscar/', buscar, name='buscar'),
    path('', index, name='index'),

    # Contato (CRUD)
    path('contato/<int:id_contato>/detalhe/', contato_unico, name='contato_unico'),
    path('contato/<int:id_contato>/atualizar/', atualizar, name='atualizar'),
    path('contato/<int:id_contato>/detelar/', deletar, name='deletar'),
    path('contato/criar/', criar, name='criar'),
   
]