# Generated by Django 4.2.3 on 2023-07-19 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_delete_adddesignation_alter_adddepartment_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adddepartment',
            old_name='name',
            new_name='full_name',
        ),
    ]
