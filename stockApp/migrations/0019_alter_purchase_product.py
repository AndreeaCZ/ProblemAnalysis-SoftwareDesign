# Generated by Django 4.0.1 on 2022-01-16 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0018_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockApp.product'),
        ),
    ]
