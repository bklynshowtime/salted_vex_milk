# Generated by Django 2.0 on 2018-01-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_auto_20180119_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='max_light',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='minutes_played',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
