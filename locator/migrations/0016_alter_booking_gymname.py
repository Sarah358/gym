# Generated by Django 4.0 on 2022-01-07 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0015_package_booking_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='gymname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locator.package'),
        ),
    ]
