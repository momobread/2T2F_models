# Generated by Django 4.2.6 on 2023-10-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
        ('products', '0006_remove_product_image_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(blank=True, to='photos.photo'),
        ),
    ]