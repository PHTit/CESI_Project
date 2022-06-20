# Generated by Django 4.0.5 on 2022-06-20 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_description'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AddField(
            model_name='student',
            name='DNI',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='course.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='date_start',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student',
            name='first_time',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], default='Si', max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='how',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='student',
            name='mail',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='rate',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
