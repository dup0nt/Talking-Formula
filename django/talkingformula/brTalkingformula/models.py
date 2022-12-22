# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Circuito(models.Model):
    circuitoid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512, blank=True, null=True)
    criadoem = models.DateField(blank=True, null=True)
    comprimento = models.FloatField(blank=True, null=True)
    curvas = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuito'


class Comentario(models.Model):
    comentarioid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, blank=True, null=True)
    corpo = models.CharField(max_length=2000, blank=True, null=True)
    criadoem = models.DateField(blank=True, null=True)
    corrida_ronda = models.ForeignKey('Corrida', models.DO_NOTHING, db_column='corrida_ronda')
    noticia_noticiaid = models.ForeignKey('Noticia', models.DO_NOTHING, db_column='noticia_noticiaid')
    noticia_circuito_circuitoid = models.IntegerField()
    noticia_corrida_ronda = models.IntegerField()
    noticia_construtor_construtorid = models.BigIntegerField()
    noticia_piloto_pilotoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comentario'
        unique_together = (('comentarioid', 'corrida_ronda', 'noticia_noticiaid', 'noticia_circuito_circuitoid', 'noticia_corrida_ronda', 'noticia_construtor_construtorid', 'noticia_piloto_pilotoid'),)


class Construtor(models.Model):
    construtorid = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=512, blank=True, null=True)
    nacionalidade = models.CharField(max_length=512, blank=True, null=True)
    logo = models.CharField(max_length=512, blank=True, null=True)
    criadoem = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construtor'


class Corrida(models.Model):
    ronda = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    voltas = models.IntegerField(blank=True, null=True)
    temperatura = models.IntegerField(blank=True, null=True)
    temperaturacircuito = models.IntegerField(blank=True, null=True)
    precipitacao = models.IntegerField(blank=True, null=True)
    humidade = models.IntegerField(blank=True, null=True)
    exposicaosolar = models.IntegerField(blank=True, null=True)
    epoca_ano = models.ForeignKey('Epoca', models.DO_NOTHING, db_column='epoca_ano')
    circuito_circuitoid = models.ForeignKey(Circuito, models.DO_NOTHING, db_column='circuito_circuitoid')

    class Meta:
        managed = False
        db_table = 'corrida'


class Epoca(models.Model):
    ano = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'epoca'


class Equipa(models.Model):
    equipaid = models.BigAutoField(primary_key=True)
    chefe = models.CharField(max_length=512, blank=True, null=True)
    chefetecnico = models.CharField(max_length=512, blank=True, null=True)
    chassis = models.CharField(max_length=512, blank=True, null=True)
    foto_carro = models.CharField(max_length=512, blank=True, null=True)
    construtor_construtorid = models.ForeignKey(Construtor, models.DO_NOTHING, db_column='construtor_construtorid')
    epoca_ano = models.ForeignKey(Epoca, models.DO_NOTHING, db_column='epoca_ano')

    class Meta:
        managed = False
        db_table = 'equipa'
        unique_together = (('equipaid', 'construtor_construtorid'),)


class Noticia(models.Model):
    noticiaid = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    corpo = models.CharField(max_length=5000, blank=True, null=True)
    foto = models.CharField(max_length=512, blank=True, null=True)
    criadoem = models.DateField(blank=True, null=True)
    circuito_circuitoid = models.ForeignKey(Circuito, models.DO_NOTHING, db_column='circuito_circuitoid')
    corrida_ronda = models.ForeignKey(Corrida, models.DO_NOTHING, db_column='corrida_ronda')
    construtor_construtorid = models.ForeignKey(Construtor, models.DO_NOTHING, db_column='construtor_construtorid')
    piloto_pilotoid = models.ForeignKey('Piloto', models.DO_NOTHING, db_column='piloto_pilotoid')

    class Meta:
        managed = False
        db_table = 'noticia'
        unique_together = (('noticiaid', 'circuito_circuitoid', 'corrida_ronda', 'construtor_construtorid', 'piloto_pilotoid'),)


class Piloto(models.Model):
    pilotoid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512, blank=True, null=True)
    nacionalidade = models.CharField(max_length=512, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    foto = models.CharField(max_length=512, blank=True, null=True)
    equipa_equipaid = models.ForeignKey(Equipa, models.DO_NOTHING, db_column='equipa_equipaid')
    equipa_construtor_construtorid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'piloto'


class Resultados(models.Model):
    resultadoid = models.AutoField(primary_key=True)
    posinicio = models.IntegerField()
    posfinal = models.IntegerField(blank=True, null=True)
    tempototal = models.IntegerField(blank=True, null=True)
    voltarapida = models.IntegerField(blank=True, null=True)
    corrida_ronda = models.ForeignKey(Corrida, models.DO_NOTHING, db_column='corrida_ronda')
    piloto_pilotoid = models.ForeignKey(Piloto, models.DO_NOTHING, db_column='piloto_pilotoid')

    class Meta:
        managed = False
        db_table = 'resultados'
        unique_together = (('resultadoid', 'corrida_ronda', 'piloto_pilotoid'),)
