# Generated by Django 3.1.5 on 2021-01-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20210127_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionsofday',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Комментарий'),
        ),
    ]
