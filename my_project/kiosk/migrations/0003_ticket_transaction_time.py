# Generated by Django 5.1.4 on 2024-12-14 09:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0002_ticket_certificate_type_ticket_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='transaction_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
