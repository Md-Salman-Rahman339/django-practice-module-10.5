# Generated by Django 4.2.7 on 2023-12-08 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskcategory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcategory',
            name='category',
        ),
    ]
