# Generated by Django 4.2.17 on 2025-01-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]
