# Generated by Django 2.0 on 2018-02-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvestats', '0002_auto_20180203_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pvestats',
            name='average_life',
            field=models.IntegerField(null=True),
        ),
    ]
