# Generated by Django 3.2.8 on 2021-10-17 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211011_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='saller',
            new_name='seller',
        ),
    ]