# Generated by Django 4.0.3 on 2022-03-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_alter_job_applicants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.ImageField(upload_to='images'),
        ),
    ]
