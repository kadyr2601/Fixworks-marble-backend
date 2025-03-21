# Generated by Django 5.1.6 on 2025-02-22 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_big', models.ImageField(upload_to='about/')),
                ('image_small', models.ImageField(upload_to='about/')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='ClientsEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Clients Email',
                'verbose_name_plural': 'Clients Emails',
            },
        ),
        migrations.CreateModel(
            name='ClientsReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('review', models.TextField()),
                ('fullname', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='clients/')),
            ],
            options={
                'verbose_name': 'Clients Review',
                'verbose_name_plural': 'Clients Reviews',
            },
        ),
        migrations.CreateModel(
            name='GetInContactSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Get In Contact Section',
                'verbose_name_plural': 'Get In Contact Section',
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('image', models.ImageField(upload_to='projects/')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='WhatOurClientsSay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('fullname', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='clients/')),
            ],
            options={
                'verbose_name': 'What Our Clients Say',
                'verbose_name_plural': 'What Our Clients Say',
            },
        ),
        migrations.CreateModel(
            name='SubActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subTitle', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_activities', to='api.activity')),
            ],
        ),
    ]
