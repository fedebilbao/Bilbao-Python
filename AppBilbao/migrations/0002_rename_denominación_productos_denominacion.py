# Generated by Django 5.0.6 on 2024-06-05 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBilbao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='denominación',
            new_name='denominacion',
        ),
    ]
