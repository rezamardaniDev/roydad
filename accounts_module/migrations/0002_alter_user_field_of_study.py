# Generated by Django 5.0.2 on 2024-02-20 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='field_of_study',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_module.field', verbose_name='رشته تحصیلی'),
        ),
    ]