# Generated by Django 4.0.1 on 2022-01-14 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0010_order_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='item',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
