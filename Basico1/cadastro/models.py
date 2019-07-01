from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dtcriacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    observacoes = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Transações"

    def __str__(self):
        return self.descricao + " - "+ str(self.data)