# Generated by Django 4.0 on 2022-01-07 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0009_alter_booking_gymname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='gymname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locator.location'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locator.package'),
        ),
        migrations.AlterField(
            model_name='package',
            name='gymname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locator.location'),
        ),
    ]
