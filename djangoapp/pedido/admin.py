from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'total',
        'status',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'id',
        'usuario__username',
    )

    inlines = [
        ItemPedidoInline,
    ]


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pedido',
        'produto',
        'variacao',
        'preco',
        'quantidade',
    )

    search_fields = (
        'produto',
        'variacao',
    )