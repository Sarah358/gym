# Generated by Django 4.0 on 2022-01-07 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0003_packages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='packagename',
            new_name='name',
        ),
    ]