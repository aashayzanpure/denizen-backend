# Generated by Django 2.2.4 on 2020-02-16 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0036_auto_20191028_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(blank=True, default=None, max_length=14, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('direction', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
