# Generated by Django 4.0.4 on 2022-08-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='short_name',
            field=models.CharField(max_length=20),
        ),
    ]
