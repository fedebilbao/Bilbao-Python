# Generated by Django 5.0.6 on 2024-06-15 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBilbao', '0002_rename_denominación_productos_denominacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(default='https://dummyimage.com/450x300/dee2e6/6c757d.jpg', upload_to=None, verbose_name=''),
        ),
    ]