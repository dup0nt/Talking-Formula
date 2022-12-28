# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    nome = models.CharField(max_length=80)
    corpo = models.CharField(max_length=2000)
    criadoem = models.DateTimeField(auto_now_add=True)
    noticia_noticiaid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comentario'
        unique_together = (('comentarioid', 'noticia_noticiaid'),)
        ordering = ['criadoem']
    
    def __str__(self):
        return 'Comentado por {} a {}'.format(self.nome, self.criadoem)

class Construtor(models.Model):
    construtorid = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=512, blank=True)
    nacionalidade = models.CharField(max_length=512, blank=True)
    logo = models.CharField(max_length=512, blank=True)
    criadoem = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construtor'


class Corrida(models.Model):
    ronda = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512)
    voltas = models.IntegerField(blank=True, null=True)
    ocorreem = models.DateField(blank=True, null=True)
    horas = models.CharField(max_length=512)
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
        ordering = ['ocorreem']


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    foto = models.CharField(max_length=512)
    criadoem = models.DateField()

    class Meta:
        managed = False
        db_table = 'noticia'
        ordering = ['-criadoem'] 



class Piloto(models.Model):
    pilotoid = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=512, blank=True, null=True)
    nacionalidade = models.CharField(max_length=512, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    foto = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'piloto'


class PilotoEquipa(models.Model):
    piloto_pilotoid = models.OneToOneField(Piloto, models.DO_NOTHING, db_column='piloto_pilotoid', primary_key=True)
    equipa_equipaid = models.ForeignKey(Equipa, models.DO_NOTHING, db_column='equipa_equipaid')
    equipa_construtor_construtorid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'piloto_equipa'
        unique_together = (('piloto_pilotoid', 'equipa_equipaid', 'equipa_construtor_construtorid'),)


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
        #ordering = ['posfinal']

    


class ResultadoPontos(models.Model):
    posfinal = models.AutoField(primary_key=True)
    pontos = models.IntegerField()

    class Meta:
        db_table = 'resultado_pontos'