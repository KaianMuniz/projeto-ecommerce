from django import template
from utils.formatting import utils_formata_preco

register = template.Library()


@register.filter
def formata_preco(valor):
    return utils_formata_preco(valor)