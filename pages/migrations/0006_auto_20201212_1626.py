# Generated by Django 3.1.4 on 2020-12-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201212_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odpad',
            name='month',
            field=models.CharField(choices=[('JAN', 'Januar'), ('FEB', 'Februar'), ('MAR', 'Marec'), ('APR', 'April'), ('MÁJ', 'Maj'), ('JÚN', 'Jun'), ('JÚL', 'Jul'), ('AUG', 'August'), ('SEP', 'September'), ('OKT', 'Oktober'), ('NOV', 'November'), ('DEC', 'December')], default='', max_length=200),
        ),
    ]
