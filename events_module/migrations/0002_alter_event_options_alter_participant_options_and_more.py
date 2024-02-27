# Generated by Django 5.0.2 on 2024-02-22 13:18

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'رویداد', 'verbose_name_plural': 'رویدادها'},
        ),
        migrations.AlterModelOptions(
            name='participant',
            options={'verbose_name': 'شرکت کننده', 'verbose_name_plural': 'شرکت کنندگان'},
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=django_jalali.db.models.jDateField(verbose_name='تاریخ شروع'),
        ),
    ]