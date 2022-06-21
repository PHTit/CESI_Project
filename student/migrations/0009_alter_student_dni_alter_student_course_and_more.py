# Generated by Django 4.0.5 on 2022-06-21 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_course_when'),
        ('student', '0008_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DNI',
            field=models.CharField(default='', max_length=15, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.course', verbose_name='Actividad'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_time',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=2, verbose_name='Primera vez en SECI?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='how',
            field=models.CharField(default='', max_length=40, verbose_name='Cómo nos conociste?'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=40, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mail',
            field=models.EmailField(default='', max_length=254, verbose_name='Mail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=40, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(default='', max_length=15, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='student',
            name='rate',
            field=models.IntegerField(default='0', verbose_name='Aporte económico'),
        ),
    ]
