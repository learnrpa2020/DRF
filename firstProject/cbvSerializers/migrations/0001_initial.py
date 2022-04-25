# Generated by Django 3.2.5 on 2022-04-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=25)),
                ('ratings', models.IntegerField()),
            ],
        ),
    ]
