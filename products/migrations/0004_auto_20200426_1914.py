# Generated by Django 3.0.5 on 2020-04-26 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_has_sized'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_sized',
            new_name='has_sizes',
        ),
    ]
