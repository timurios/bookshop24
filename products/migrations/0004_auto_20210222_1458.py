# Generated by Django 3.1.7 on 2021-02-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(height_field=200, upload_to='main.html', verbose_name='D:\\Desktop\\project\\ShowCover.jpg', width_field=100),
        ),
    ]