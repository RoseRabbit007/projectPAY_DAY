# Generated by Django 4.2.3 on 2023-07-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0004_alter_bank_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_code',
            field=models.BigIntegerField(unique=True),
        ),
    ]
