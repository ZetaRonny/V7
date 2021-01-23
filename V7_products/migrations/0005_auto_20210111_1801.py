# Generated by Django 3.0.7 on 2021-01-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('V7_products', '0004_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]