# Generated by Django 2.1 on 2019-03-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorental', '0003_auto_20190320_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='rented',
        ),
        migrations.AddField(
            model_name='movie',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]
