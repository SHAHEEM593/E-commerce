# Generated by Django 4.2.2 on 2023-06-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
