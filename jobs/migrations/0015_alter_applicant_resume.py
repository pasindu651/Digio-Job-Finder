# Generated by Django 4.0.3 on 2022-03-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_alter_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
