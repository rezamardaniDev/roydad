# Generated by Django 5.0.2 on 2024-02-26 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_module', '0004_field_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='username',
        ),
    ]