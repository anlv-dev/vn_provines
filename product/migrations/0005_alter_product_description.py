# Generated by Django 4.0.4 on 2022-08-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='This is a product that many people love in 2022.', max_length=500),
        ),
    ]
