# Generated by Django 3.2.13 on 2022-11-21 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_image_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
