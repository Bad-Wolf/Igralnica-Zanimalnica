# Generated by Django 2.2.1 on 2019-05-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_auto_20190528_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choices',
            name='type',
        ),
        migrations.AddField(
            model_name='choices',
            name='igralnica',
            field=models.BooleanField(default=False, verbose_name='игралница'),
        ),
        migrations.AddField(
            model_name='choices',
            name='zanimalnica',
            field=models.BooleanField(default=False, verbose_name='занималница'),
        ),
    ]
