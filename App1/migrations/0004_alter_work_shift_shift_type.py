# Generated by Django 4.1.7 on 2023-07-19 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_alter_work_shift_shift_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_shift',
            name='shift_type',
            field=models.CharField(choices=[('Regular Work Shift', 'Regular Work Shift '), ('Demo working Shift regular', 'Demo working Shift regular'), ('demo working shift sheduled', 'Demo working shift sheduled')], default=True, max_length=100),
        ),
    ]