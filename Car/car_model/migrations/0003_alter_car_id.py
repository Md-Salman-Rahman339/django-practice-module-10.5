# Generated by Django 4.2.7 on 2023-12-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_model', '0002_car_author_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
