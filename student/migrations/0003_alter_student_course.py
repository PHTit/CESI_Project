# Generated by Django 4.0.5 on 2022-06-20 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_description'),
        ('student', '0002_remove_student_email_student_dni_student_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.course'),
        ),
    ]