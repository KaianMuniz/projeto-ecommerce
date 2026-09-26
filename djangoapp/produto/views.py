from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages
from . import models


# Create your views here.

class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10

class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AdicionarProduto(View):
    def get(self,*args,**kwargs): 
        vid = self.request.GET.get('vid')

        if not vid:
            messages.error(self.request,'Produto não existe',)
            return redirect('produto:lista')

        variacao = get_object_or_404(models.Variacao,id=vid)
        

        redirect_produto = redirect('produto:detalhe' ,slug=variacao.produto.slug)

        if variacao.estoque < 1:
            messages.error(
                self.request,'Estoque insuficiente'
            )
            return redirect_produto

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            

        carrinho = self.request.session['carrinho']

        if vid in carrinho:
            qnt_carrinho = carrinho[vid]['quantidade']
            qnt_carrinho += 1

            if variacao.estoque < qnt_carrinho:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {qnt_carrinho}x no '
                    f'produto {variacao.produto.nome}. Adicionamos {variacao.estoque}x '
                    f'no seu carrinho. '
                )
                return redirect_produto
            
            carrinho[vid]['quantidade'] = qnt_carrinho
            carrinho[vid]['preco_quantitativo'] = variacao.preco * qnt_carrinho
            carrinho[vid]['preco_quantitativo_promocional'] = variacao.preco_promocional * qnt_carrinho
        else:
            carrinho[vid] = {
                'produto_id': variacao.produto.pk,
                'produto_nome': variacao.produto.nome,
                'variacao_id': variacao.pk,
                'variacao_nome': variacao.nome,
                'preco_unitario': variacao.preco,
                'preco_unitario_promocional': variacao.preco_promocional,
                'preco_quantitativo' : variacao.preco,
                'preco_quantitativo_promocional' : variacao.preco_promocional,
                'quantidade': 1,
                'slug': variacao.produto.slug,
                'imagem': variacao.produto.imagem.name,
            }

        self.request.session.save()
        messages.success(
            self.request,
            f'Produto {variacao.produto.nome} adicionado ao seu carrinho.'
        )
        return redirect_produto

class RemoverProduto(View):
    pass

class Carrinho(View):
    def get(self,*ars,**kwargs):
        return render(self.request,'produto/carrinho.html')

class Finalizar(View):
    pass