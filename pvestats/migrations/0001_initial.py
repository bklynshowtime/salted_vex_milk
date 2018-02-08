# Generated by Django 2.0 on 2018-02-03 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0017_member_date_last_played'),
    ]

    operations = [
        migrations.CreateModel(
            name='PveStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('number_activities', models.IntegerField(null=True)),
                ('activities_cleared', models.IntegerField(null=True)),
                ('seconds_played', models.IntegerField(null=True)),
                ('kd', models.FloatField(null=True)),
                ('favorite_weapon', models.CharField(max_length=20, null=True)),
                ('longest_spree', models.IntegerField(null=True)),
                ('most_precision_kills', models.IntegerField(null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
            options={
                'verbose_name_plural': 'PvE Stats',
            },
        ),
    ]