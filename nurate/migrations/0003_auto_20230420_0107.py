# Generated by Django 3.1.7 on 2023-04-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurate', '0002_auto_20230420_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='content',
            field=models.FileField(upload_to='staticfiles'),
        ),
    ]
