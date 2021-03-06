# Generated by Django 2.2.4 on 2019-09-04 09:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_amenity_booking_comment_complaint_entry_group_notice_payment_securitydesk_securitypersonnel_servicev'),
    ]

    operations = [
        migrations.AddField(
            model_name='township',
            name='application_id',
            field=models.CharField(default='0', max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='township',
            name='registration_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 4, 9, 26, 8, 587073, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='township',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
