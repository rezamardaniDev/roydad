# Generated by Django 5.0.2 on 2024-02-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_module', '0013_remove_discount_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='status',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
        ),
    ]
