# Generated by Django 3.0.7 on 2020-12-11 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('V7_products', '0002_auto_20201206_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='image',
        ),
    ]