# Generated by Django 2.1 on 2019-03-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]