# Generated by Django 2.2.24 on 2021-07-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
