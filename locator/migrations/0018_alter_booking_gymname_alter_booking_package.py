# Generated by Django 4.0 on 2022-01-08 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0017_alter_booking_gymname_alter_booking_package_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='gymname',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='booking',
            name='package',
            field=models.CharField(max_length=50),
        ),
    ]
