# Generated by Django 4.1.7 on 2023-04-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_enrollment', '0003_alter_enrolled_device_lock_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolled_device',
            name='qrcode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
