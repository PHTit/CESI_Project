from cgi import print_exception
from django.db import models


class Course(models.Model):
    TYPES = (
        ('AB', 'AB'),
        ('CO', 'CO'),
        ('GE', 'GE'),
    )
    name = models.CharField(max_length=40)
    description = models.TextField(blank = True, null=True)
    owner = models.CharField(max_length=40)
    teacher = models.CharField(max_length=40)
    price = models.IntegerField
    type = models.CharField(max_length=2, choices=TYPES)
    date_start = models.DateField


    def __str__(self):
        return f'{self.name}'