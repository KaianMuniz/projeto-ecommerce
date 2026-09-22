from django.db import models
from utils.image import resize_image

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='products/%Y/%m/',blank=True,null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(('V','Variação'),('S','Simples'))
    )

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        if self.imagem:
            resize_image(self.imagem)

    def __str__(self):
        return self.nome

class Variacao(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

    def __str__(self):
        return self.nome or self.produto.nome
    