# Generated by Django 4.0.3 on 2022-03-18 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_job_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='date',
            new_name='time',
        ),
    ]
