# Generated by Django 5.1.7 on 2025-03-28 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='сategory',
            new_name='category',
        ),
    ]
