from cgi import print_exception
from django.db import models

class Course(models.Model):
    TYPES = (('AB', 'AB'),('CO', 'CO'),('GE', 'GE'))
    name = models.CharField(max_length=40, default="", verbose_name="Nombre")
    when = models.CharField(max_length=100, default="", verbose_name="Cuándo se dicta?")
    description = models.TextField(blank = True, null=True, default="", verbose_name="Descripción")
    owner = models.CharField(max_length=40, default="", verbose_name="Titular")
    teacher = models.CharField(max_length=40, default="", verbose_name="Docente")
    price = models.IntegerField(verbose_name="Aporte económico")
    type = models.CharField(max_length=2,default="", choices=TYPES, verbose_name="Tipo")
    

    def __str__(self):
        return f'{self.name}'