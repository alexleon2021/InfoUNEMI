from django.db import models
#creacion de los modelos 

class Sitio(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre del Sitio',max_length=100,null = False ,blank= False)
    Bloques = models.ForeignKey('Bloque', on_delete=models.PROTECT, default="", blank= False)
    horario = models.CharField('Horario de atencion',max_length=100, blank= True)
    foto = models.URLField('foto',null = False ,blank= True)
    gps = models.CharField(max_length=100, blank= False)
    
    class Meta:
        verbose_name = 'Sitio'
        verbose_name_plural = 'Sitios'
    
    def __str__(self):
        return self.nombre

class Bloque(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre del bloque',max_length=100,null = False ,blank= False)
    funciones = models.CharField('Funciones del Bloque',max_length=100)
    nombre_encargado = models.CharField('Nombre del encargado',max_length=100, blank= True)
    numero_planta = models.IntegerField('numero de plantas')
    horario_bloque = models.CharField('Horarios',max_length=100)
    descripcion = models.TextField(null = True, blank=True)


    class Meta:
        verbose_name = 'Bloque'
        verbose_name_plural = 'Bloques'

    def __str__(self):
        return self.nombre