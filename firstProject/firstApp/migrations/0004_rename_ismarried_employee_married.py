# Generated by Django 3.2.5 on 2022-04-24 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_employee_ismarried'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='isMarried',
            new_name='married',
        ),
    ]