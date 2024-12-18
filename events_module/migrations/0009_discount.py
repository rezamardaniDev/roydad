# Generated by Django 5.0.2 on 2024-02-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_module', '0008_alter_event_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250, null=True, verbose_name='کد تخفیف')),
                ('percent', models.IntegerField(null=True, verbose_name='درصد تخفیف')),
                ('count', models.IntegerField(null=True, verbose_name='تعداد استفاده')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کدهای تخفیف',
            },
        ),
    ]
