# Generated by Django 4.1.5 on 2023-01-27 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='dname',
            new_name='district',
        ),
    ]
