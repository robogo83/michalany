# Generated by Django 3.1.4 on 2020-12-30 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_zapisnicefiles_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zapisnicefiles',
            name='typ',
        ),
    ]
