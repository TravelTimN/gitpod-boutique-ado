# Generated by Django 3.0.5 on 2020-04-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200424_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_sized',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]