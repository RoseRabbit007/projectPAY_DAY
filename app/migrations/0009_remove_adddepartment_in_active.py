# Generated by Django 4.2.3 on 2023-07-19 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_new_active_adddepartment_in_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adddepartment',
            name='in_active',
        ),
    ]