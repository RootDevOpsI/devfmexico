# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assistants',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name_assistants', models.CharField(max_length=255)),
                ('phone_assistants', models.IntegerField()),
                ('email_assistants', models.EmailField(max_length=254)),
                ('address_assistants', models.TextField()),
                ('timestamp', models.DateField(auto_now=True)),
                ('fkstore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assistants', to='stores.Store')),
            ],
        ),
    ]