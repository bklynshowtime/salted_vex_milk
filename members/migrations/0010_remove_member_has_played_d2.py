# Generated by Django 2.0 on 2017-12-22 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_member_has_played_d2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='has_played_d2',
        ),
    ]
