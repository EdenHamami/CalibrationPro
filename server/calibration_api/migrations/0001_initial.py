# Generated by Django 5.1.4 on 2024-12-27 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('device_name', models.CharField(blank=True, max_length=255, null=True)),
                ('device_features', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'devices',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'models',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_date', models.DateField()),
                ('input_value', models.DecimalField(decimal_places=4, max_digits=10)),
                ('output_value', models.DecimalField(decimal_places=4, max_digits=10)),
                ('unit1', models.CharField(max_length=50)),
                ('deviation', models.DecimalField(decimal_places=4, max_digits=10)),
                ('tolerance', models.DecimalField(decimal_places=4, max_digits=10)),
                ('unit2', models.CharField(blank=True, max_length=50, null=True)),
                ('uncertainty', models.DecimalField(decimal_places=4, max_digits=10)),
                ('unit3', models.CharField(blank=True, max_length=50, null=True)),
                ('threshold', models.DecimalField(decimal_places=4, max_digits=10)),
                ('identifier', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calibration_api.device')),
            ],
            options={
                'db_table': 'measurements',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calibration_api.model'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calibration_api.user'),
        ),
    ]
