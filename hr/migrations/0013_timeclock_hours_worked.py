# Generated by Django 5.1.6 on 2025-03-07 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0012_timeclock'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeclock',
            name='hours_worked',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
