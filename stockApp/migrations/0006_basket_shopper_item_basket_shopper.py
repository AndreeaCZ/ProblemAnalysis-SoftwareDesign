# Generated by Django 4.0.1 on 2022-01-13 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Shopper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='stockApp.product')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockApp.basket')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='shopper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockApp.shopper'),
        ),
    ]
