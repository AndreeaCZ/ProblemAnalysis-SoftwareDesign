# Generated by Django 4.0.1 on 2022-01-15 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockApp', '0015_remove_purchase_item_remove_purchase_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('shopper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockApp.shopper')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stockApp.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockApp.order')),
            ],
        ),
    ]
