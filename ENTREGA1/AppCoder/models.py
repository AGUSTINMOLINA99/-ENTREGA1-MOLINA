from django.db import models

# Create your models here.

class Integrate(models.Model):
    nombre=models.charField(max_length=40)
    fecnac=models.DateField()
    telefono=models.IntegerField()
    