# Generated by Django 4.2.1 on 2023-07-12 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bidding', '0009_alter_bid_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 12, 19, 1, 19, 433238), null=True),
        ),
    ]