# Generated by Django 3.2 on 2022-06-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.IntegerField(max_length=10),
        ),
    ]
