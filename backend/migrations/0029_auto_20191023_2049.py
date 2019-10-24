# Generated by Django 2.2.4 on 2019-10-23 15:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0028_visitor_township'),
    ]

    operations = [
        migrations.AddField(
            model_name='securitydesk',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='securitydesk',
            name='township',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Township'),
        ),
        migrations.AddField(
            model_name='securitypersonnel',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='securitypersonnel',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='securitypersonnel',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='securitypersonnel',
            name='shift_days',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='securitypersonnel',
            name='shift_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='securitypersonnel',
            name='shift_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='securitypersonnel',
            name='township',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Township'),
        ),
    ]
