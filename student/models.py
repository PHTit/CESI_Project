from django.db import models



class Student(models.Model):
    FIRST = (('Si','Si'),('No','No'))
    
    name = models.CharField(max_length=40, default="")
    last_name = models.CharField(max_length=40, default="")
    DNI = models.CharField(max_length=15, default="")
    mail = models.EmailField(default="")
    phone = models.CharField(max_length=15, default="")
    first_time = models.CharField(max_length=2, choices=FIRST, default="Si")
    how = models.CharField(max_length=40, default="")
    rate = models.IntegerField(default="0")
    date_start = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Nombre del Alumno: {self.name} {self.last_name}'