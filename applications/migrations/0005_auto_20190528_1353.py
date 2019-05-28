# Generated by Django 2.2.1 on 2019-05-28 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_childapplication_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('I', 'Игралница'), ('Z', 'Занималница')], max_length=1, verbose_name='тип')),
            ],
        ),
        migrations.RemoveField(
            model_name='childapplication',
            name='type',
        ),
        migrations.AddField(
            model_name='childapplication',
            name='type',
            field=models.ManyToManyField(to='applications.Choices'),
        ),
    ]
