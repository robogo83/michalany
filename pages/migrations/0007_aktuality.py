# Generated by Django 3.1.4 on 2020-12-16 22:48

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20201212_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktuality',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=350)),
                ('date', models.DateField(auto_now=True)),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'aktuality',
            },
        ),
    ]
