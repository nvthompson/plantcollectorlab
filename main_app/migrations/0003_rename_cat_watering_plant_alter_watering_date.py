# Generated by Django 4.0.2 on 2022-02-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watering'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watering',
            old_name='cat',
            new_name='plant',
        ),
        migrations.AlterField(
            model_name='watering',
            name='date',
            field=models.DateField(verbose_name='watering date'),
        ),
    ]
