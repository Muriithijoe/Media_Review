# Generated by Django 2.2.3 on 2019-07-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreview',
            name='business_daily',
            field=models.TextField(default='null=False', max_length=500),
            preserve_default=False,
        ),
    ]
