# Generated by Django 2.2.4 on 2019-08-19 10:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
