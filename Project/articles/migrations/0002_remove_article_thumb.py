# Generated by Django 2.0.6 on 2018-06-27 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
    ]
