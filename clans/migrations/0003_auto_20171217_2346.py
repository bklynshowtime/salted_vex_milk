# Generated by Django 2.0 on 2017-12-17 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clans', '0002_auto_20171217_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='creation_date',
            field=models.CharField(max_length=100),
        ),
    ]
