from django.db import models
import datetime

class Fotografia(models.Model):

    opcoes_de_categoria = [
        ('nebulosa', 'Naisagem'),
        ('estrela', 'Estrela'),
        ('galaxia', 'Galaxia'),
        ('planeta', 'Planeta'),

    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.CharField(max_length=50,choices=opcoes_de_categoria, default='nebulosa')
    descricao = models.TextField(null=True, blank=True)
    foto = models.CharField(max_length=255, null=False, blank=False)
    publicada  = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.datetime.now, null=False, blank=False)

    def __str__(self):
        return f"Fotografia - {self.nome}  - {self.legenda if self.legenda else 'Sem legenda'}"