# Generated by Django 4.2.17 on 2025-01-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('intern_id', models.IntegerField(primary_key=True, serialize=False)),
                ('intern_name', models.CharField(max_length=50)),
                ('intern_city', models.CharField(max_length=50)),
                ('intern_phone', models.CharField(max_length=50)),
            ],
        ),
    ]
