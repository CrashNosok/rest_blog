# Generated by Django 3.1.3 on 2020-11-07 20:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='when_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 7, 20, 12, 38, 250593, tzinfo=utc)),
        ),
    ]