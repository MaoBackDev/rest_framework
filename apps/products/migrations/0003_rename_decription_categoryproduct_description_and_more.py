# Generated by Django 4.1.6 on 2023-02-13 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryproduct',
            old_name='decription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='historicalcategoryproduct',
            old_name='decription',
            new_name='description',
        ),
    ]
