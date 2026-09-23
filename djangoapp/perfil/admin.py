from django.contrib import admin

from .models import Perfil, Endereco


class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'cpf',
        'data_nascimento',
        'idade',
    )

    search_fields = (
        'usuario__username',
        'cpf',
    )

    inlines = [
        EnderecoInline,
    ]