# Generated by Django 2.0 on 2018-02-16 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_member_date_last_played'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_joined',
            field=models.DateTimeField(),
        ),
    ]
