# Generated by Django 2.2.1 on 2019-05-22 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_picture_picturecomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PictureComment',
        ),
    ]