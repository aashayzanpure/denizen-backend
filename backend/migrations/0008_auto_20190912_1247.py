# Generated by Django 2.2.4 on 2019-09-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190907_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='township',
            name='geo_address',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
