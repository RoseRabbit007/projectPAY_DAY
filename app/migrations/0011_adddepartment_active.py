# Generated by Django 4.2.3 on 2023-07-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_adddesignation'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddepartment',
            name='active',
            field=models.BooleanField(blank=True, max_length=100, null=True),
        ),
    ]