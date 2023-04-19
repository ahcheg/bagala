# Generated by Django 3.1.7 on 2023-04-19 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('parent_school', models.CharField(choices=[('1', 'SEDS'), ('2', 'SSH'), ('3', 'SMG'), ('4', 'SME'), ('5', 'Graduate')], default=1, max_length=32)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('parent_course_category', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('date_uploaded', models.DateField()),
                ('content', models.FileField(upload_to='')),
                ('parent_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurate.courses')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]
