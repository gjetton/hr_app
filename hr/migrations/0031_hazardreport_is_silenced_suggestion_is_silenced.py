# Generated by Django 5.1.6 on 2025-03-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0030_alter_employeecertification_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hazardreport',
            name='is_silenced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='is_silenced',
            field=models.BooleanField(default=False),
        ),
    ]
