# Generated by Django 4.2.2 on 2023-06-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'Basic'), (1, 'Manger'), (2, 'Driver')], default=0),
        ),
    ]
