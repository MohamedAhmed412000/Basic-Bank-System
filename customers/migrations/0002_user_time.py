# Generated by Django 4.0 on 2022-02-19 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 19, 17, 6, 51, 277345)),
        ),
    ]
