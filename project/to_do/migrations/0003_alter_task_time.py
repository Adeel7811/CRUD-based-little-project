# Generated by Django 5.1 on 2024-08-29 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_alter_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
