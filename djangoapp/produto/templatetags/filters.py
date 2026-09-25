from django import template
from utils.formatting import utils_formata_preco

register = template.Library()


@register.filter
def formata_preco(valor):
    return utils_formata_preco(valor)

@register.filter
def primeira_variacao(variacoes):
    return variacoes.order_by('pk').first()

@register.filter
def tem_promocao(variacoes):
    return variacoes.filter(
        preco_promocional__gt=0
    ).exists()