# Generated by Django 4.2.7 on 2023-12-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_model', '0016_buycar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
