# Generated by Django 4.2.1 on 2023-07-13 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_product_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 13, 8, 53, 54, 93261), null=True),
        ),
    ]
