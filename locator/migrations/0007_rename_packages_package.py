# Generated by Django 4.0 on 2022-01-07 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0006_rename_book_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Packages',
            new_name='Package',
        ),
    ]
