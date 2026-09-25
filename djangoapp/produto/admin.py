from django.contrib import admin

from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'nome',
        'tipo',
    )

    list_display_links = (
        'id',
        'nome',
    )

    list_filter = (
        'tipo',
    )

    search_fields = (
        'nome',
        'descricao_curta',
    )

    inlines = [
        VariacaoInline,
    ]

@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'produto',
        'nome',
        'preco',
        'preco_promocional',
        'estoque',
    )