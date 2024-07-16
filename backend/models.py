
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models 
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, dni, nombrey_apellido, password=None, **extra_fields):
        if not dni:
            raise ValueError('El DNI es obligatorio')
        user = self.model(dni=dni, nombrey_apellido=nombrey_apellido, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, nombrey_apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(dni, nombrey_apellido, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    idgeneral = models.CharField(max_length=50, blank=True, null=True)
    nombrey_apellido = models.CharField(max_length=100)
    jefe_inmediato = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    tipo_usurio = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombrey_apellido']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.nombrey_apellido

class DiarioDePesca(models.Model):
    embarcacion = models.IntegerField()  
    especie = models.IntegerField()
    fecha = models.DateField()
    numero_alcance = models.IntegerField()
    zona_pesca = models.CharField(max_length=255)
    estrato = models.CharField(max_length=255)
    profundidad = models.IntegerField()
    tiempo_efectivo = models.TimeField()
    rango_talla_inicial = models.IntegerField()
    rango_talla_final = models.IntegerField()
    moda = models.IntegerField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    ar = models.IntegerField()
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.embarcacion} - {self.fecha}"

class Embarcaciones(models.Model):
    nombre = models.CharField(max_length=255)

class Especies(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()

class ZonaPesca(models.Model):
    nombre = models.CharField(max_length=255)

class TarifasCostos(models.Model):
    nombre_t = models.CharField(max_length=255)
    tarifa = models.DecimalField(max_digits=9, decimal_places=4)

class Viveres(models.Model):
    embarcacion = models.IntegerField()
    costo_zarpe = models.DecimalField(max_digits=5, decimal_places=2)

class MecanismosI(models.Model):
    item = models.CharField(max_length=255)
    costo_día = models.DecimalField(max_digits=5, decimal_places=2)

class TipoDescripcion(models.Model):
    descripcion = models.CharField(max_length=255)

class CostoGalon(models.Model):
    fecha = models.DateField()
    tipo = models.ForeignKey(TipoDescripcion,on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=6, decimal_places=2)

class FlotaDP(models.Model):
    fecha = models.DateField()
    embarcacion = models.ForeignKey(Embarcaciones,on_delete=models.CASCADE)
    zona_pesca = models.ForeignKey(ZonaPesca,on_delete=models.CASCADE)
    horas_faena = models.DurationField()
    kilos_declarados = models.DecimalField(max_digits=9, decimal_places=2)
    especie = models.ForeignKey(Especies,on_delete=models.CASCADE)
 


