# Generated by Django 4.0.1 on 2022-01-15 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0016_order_purchase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]