# Generated by Django 2.0.6 on 2018-06-27 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20180627_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
    ]
