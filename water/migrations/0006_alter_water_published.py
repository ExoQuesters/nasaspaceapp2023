# Generated by Django 4.2.6 on 2023-10-05 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0005_alter_water_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='water',
            name='published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='published date'),
        ),
    ]
