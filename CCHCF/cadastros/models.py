from django.db import models

# Create your models here.
class LocalAtuacao(models.Model):
    nome = models.CharField(max_length=200)
    observacao = models.TextField()

    def __str__(self):
        return self.nome

class Gerencia(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.IntegerField()

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.IntegerField()

    def __str__(self):
        return self.nome

class Nucleo(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.IntegerField()

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.IntegerField(default=0)

    def __str__(self):
        return self.nome



class CentroCusto(models.Model):
    nome = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    gerencia = models.ForeignKey(Gerencia,on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe,on_delete=models.CASCADE)
    nucleo = models.ForeignKey(Nucleo,on_delete=models.CASCADE)
    dtFim = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.departamento.codigo)+ '.'+\
                str(self.gerencia.codigo)+'.'+\
               str(self.nucleo.codigo)+'.'+\
               str(self.equipe.codigo)+ '-' +self.nome