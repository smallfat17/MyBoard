# Generated by Django 2.1.7 on 2019-08-04 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='last_update',
            new_name='last_updated',
        ),
    ]
