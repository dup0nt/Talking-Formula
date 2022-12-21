from django.db import models

# Create your models here.
class Construtor(models.Model):
    construtorid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    nacionalidade = models.CharField(max_length=512)
    chefe = models.CharField(max_length=512)
    chefetecnico = models.CharField(max_length=512)
    logo = models.URLField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Piloto(models.Model):
    pilotoid = models.AutoField(primary_key=True)
    numero_corrida = models.IntegerField()
    nome = models.CharField(max_length=512)
    nacionalidade = models.CharField(max_length=512)
    nascimento = models.DateField()
    foto = models.URLField(max_length=500, null=True, blank=True)
    construtor = models.ForeignKey(Construtor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Circuito(models.Model):
    circuitoid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    nascimento = models.DateField()
    comprimento = models.FloatField()
    curvas = models.IntegerField()
    foto = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome

class Epoca(models.Model):
    ano = models.IntegerField(primary_key=True)

class Corrida(models.Model):
    ronda = models.IntegerField(primary_key=True)
    voltas = models.IntegerField()
    temperatura = models.IntegerField()
    temperaturacircuito = models.IntegerField()
    precipitacao = models.IntegerField()
    humidade = models.IntegerField()
    exposicaosolar = models.IntegerField()
    epoca = models.ForeignKey(Epoca, on_delete=models.CASCADE)
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Resultados(models.Model):
    resultadoid = models.AutoField(primary_key=True)
    posinicio = models.IntegerField()
    posfinal = models.IntegerField()
    tempototal = models.IntegerField()
    voltarapida = models.IntegerField()
    corrida = models.ForeignKey(Corrida, on_delete=models.CASCADE)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)

class Comentario(models.Model):
    comentarioid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    corpo = models.CharField(max_length=2000)
    criadoem = models.DateField()
    corrida = models.ForeignKey(Corrida, on_delete=models.CASCADE)


