# Generated by Django 4.2.6 on 2023-10-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0002_remove_species_river_water_species'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='water',
            name='species',
        ),
        migrations.AddField(
            model_name='water',
            name='species',
            field=models.ManyToManyField(to='water.species'),
        ),
    ]
