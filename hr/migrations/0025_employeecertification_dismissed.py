# Generated by Django 5.1.6 on 2025-03-13 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0024_certification_jobsite_employeecertification'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeecertification',
            name='dismissed',
            field=models.BooleanField(default=False, help_text='Dismiss notification for this certification'),
        ),
    ]
