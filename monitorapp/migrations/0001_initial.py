# Generated by Django 2.2.3 on 2019-07-17 07:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('media_link', models.TextField(null=True, validators=[django.core.validators.URLValidator()])),
                ('nation', models.TextField(max_length=500)),
                ('standard', models.TextField(max_length=500)),
            ],
        ),
    ]
