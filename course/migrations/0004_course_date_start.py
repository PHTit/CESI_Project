# Generated by Django 4.0.5 on 2022-06-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_rename_code_course_price_course_owner_course_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_start',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
