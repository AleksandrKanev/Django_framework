# Generated by Django 5.0.1 on 2024-01-27 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('register_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(to='app_hw_4.product')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hw_4.user')),
            ],
        ),
    ]
