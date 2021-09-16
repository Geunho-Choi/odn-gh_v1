# Generated by Django 3.2.6 on 2021-08-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buoys', '0002_alter_buoy_downtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buoy',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='buoy',
            name='x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='buoy',
            name='y',
            field=models.FloatField(default=0),
        ),
    ]
