# Generated by Django 4.0.1 on 2022-01-15 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0012_basket_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='ordered',
        ),
        migrations.AlterField(
            model_name='basket',
            name='shopper',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stockApp.shopper'),
        ),
    ]
