# Generated by Django 2.1.3 on 2019-08-21 09:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 22, 9, 33, 9, 445064, tzinfo=utc)),
        ),
    ]