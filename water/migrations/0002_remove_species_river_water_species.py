# Generated by Django 4.2.6 on 2023-10-05 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='river',
        ),
        migrations.AddField(
            model_name='water',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='water.species'),
        ),
    ]
