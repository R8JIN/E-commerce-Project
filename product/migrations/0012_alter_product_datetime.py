# Generated by Django 4.2.1 on 2023-07-12 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 12, 18, 50, 12, 65048), null=True),
        ),
    ]
