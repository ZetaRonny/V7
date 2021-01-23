# Generated by Django 3.0.7 on 2021-01-23 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('V7_products', '0005_auto_20210111_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(choices=[(0, 'Vaulted'), (1, 'Available')], default='OFA', max_length=200),
        ),
    ]