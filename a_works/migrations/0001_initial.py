# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('customer_city', models.CharField(blank=True, default=None, max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Status user',
                'verbose_name_plural': 'Status user',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('salary', models.IntegerField(blank=True, default=None, null=True)),
                ('type_salary', models.CharField(blank=True, default=None, max_length=8, null=True)),
                ('description', models.TextField()),
                ('requirements', models.TextField(default=None, null=True)),
                ('duties', models.TextField(default=None, null=True)),
                ('package_that_compensates', models.TextField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='a_works.Employer')),
                ('status', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='a_works.Status')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancys',
            },
        ),
    ]
