# Generated by Django 2.2.1 on 2019-05-18 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20190518_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='childapplication',
            old_name='email',
            new_name='user',
        ),
    ]