# Generated by Django 4.2.2 on 2023-06-23 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('carry', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carry',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='order.order'),
        ),
    ]
