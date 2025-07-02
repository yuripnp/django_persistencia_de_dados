from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    foto = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"Fotografia - {self.nome}  - {self.legenda if self.legenda else 'Sem legenda'}"