from django.urls import path
from .views import index, contato_unico

urlpatterns = [ 
    path('<int:id_contato>/', contato_unico, name='contato_unico'),
    path('', index, name='index'),
   
]