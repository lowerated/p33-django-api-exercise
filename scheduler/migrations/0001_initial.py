# Generated by Django 3.2.23 on 2024-07-19 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_status', models.CharField(max_length=50)),
                ('status_start_time', models.DateTimeField()),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.truck')),
            ],
        ),
    ]
