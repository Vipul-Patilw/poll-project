# Generated by Django 4.1.3 on 2023-01-10 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0002_alter_poll_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 12, 26, 55, 614094, tzinfo=datetime.timezone.utc)),
        ),
    ]
