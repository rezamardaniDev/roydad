# Generated by Django 5.0.2 on 2024-02-22 13:55

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_module', '0004_alter_event_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=django_jalali.db.models.jDateTimeField(verbose_name='تاریخ شروع'),
        ),
    ]
