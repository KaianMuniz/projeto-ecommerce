from django.db import models
from django.contrib.auth.models import User
from utils.validators import valida_cpf,valida_cep,valida_data_nascimento
from utils.age_calculator import calcular_idade


# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    data_nascimento = models.DateField(validators=[valida_data_nascimento])
    cpf = models.CharField(max_length=11,validators=[valida_cpf])

    @property
    def idade(self):
        return calcular_idade(self.data_nascimento)

    def __str__(self):
            return f'{self.usuario}'

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'


class Endereco(models.Model):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='enderecos'
    )

    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=9,validators=[valida_cep])
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2, choices=(
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ))

    def __str__(self):
        return f'{self.endereco}, {self.numero} - {self.cidade}/{self.estado}'