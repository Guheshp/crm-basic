# Generated by Django 5.0.1 on 2024-01-21 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_record_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='phone',
        ),
    ]
