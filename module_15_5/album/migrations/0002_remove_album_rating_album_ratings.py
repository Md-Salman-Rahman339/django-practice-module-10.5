# Generated by Django 4.2.7 on 2023-12-07 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='rating',
        ),
        migrations.AddField(
            model_name='album',
            name='ratings',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]
