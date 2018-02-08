# Generated by Django 2.0 on 2018-02-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvpstats', '0006_auto_20180131_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='pvpstats',
            name='deaths_per_match',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pvpstats',
            name='kills_per_match',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pvpstats',
            name='longest_kill_distance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pvpstats',
            name='number_wins',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pvpstats',
            name='suicides',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pvpstats',
            name='win_loss_ratio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]