# Generated by Django 2.0 on 2017-12-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_remove_member_has_played_d2'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='has_played_d2',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
