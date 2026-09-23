from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProduto.as_view(), name="detalhe"),
    path('adicionarproduto/', views.AdicionarProduto.as_view(), 
        name="adicionarproduto"),
    path('removerproduto/', views.RemoverProduto.as_view(), 
        name="removerproduto"),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho"),
    path('finalizar/', views.Finalizar.as_view(), name="finalizar"),
]

