# Generated by Django 3.1.7 on 2022-06-11 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('priority', models.CharField(blank=True, choices=[('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='None', max_length=10)),
                ('category', models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Work', 'Work'), ('Other', 'Other')], default='Other', max_length=10)),
                ('assigned_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('done', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
