# Generated by Django 2.1 on 2019-03-22 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorental', '0009_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentedMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('movie', models.ManyToManyField(to='videorental.Movie')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='rented_movies',
            field=models.ManyToManyField(to='videorental.RentedMovie'),
        ),
    ]