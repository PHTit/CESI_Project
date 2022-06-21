from django.db import models
from course.models import Course


class Student(models.Model):
    FIRST = (('Si','Si'),('No','No'))
    
    name = models.CharField(max_length=40, default="", verbose_name="Nombre")
    last_name = models.CharField(max_length=40, default="", verbose_name="Apellido")
    DNI = models.CharField(max_length=15, default="", verbose_name="DNI")
    mail = models.EmailField(default="", verbose_name="Mail")
    phone = models.CharField(max_length=15, default="", verbose_name="Teléfono")
    first_time = models.CharField(max_length=2, choices=FIRST, default="Si", verbose_name="Primera vez en SECI?")
    how = models.CharField(max_length=40, default="", verbose_name="Cómo nos conociste?")
    rate = models.IntegerField(default="0", verbose_name="Aporte económico")
    date_start = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course,null=True,blank=True,on_delete=models.DO_NOTHING,default="", verbose_name="Actividad")


    def __str__(self):
        return f'{self.name} {self.last_name}'