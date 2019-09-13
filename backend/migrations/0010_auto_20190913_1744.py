# Generated by Django 2.2.4 on 2019-09-13 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_amenity_free_for_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='amount',
        ),
        migrations.AddField(
            model_name='booking',
            name='payment',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Payment'),
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='cheque_no',
            field=models.CharField(blank=True, default=None, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='mode',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='sub_type',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='payment',
            name='transaction_id',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='type',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='township',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Township'),
        ),
        migrations.AddField(
            model_name='user',
            name='wing',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Wing'),
        ),
        migrations.AlterField(
            model_name='user',
            name='apartment',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]