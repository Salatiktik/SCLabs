# Generated by Django 4.2.1 on 2023-05-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0022_remove_session_startdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='startDate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
