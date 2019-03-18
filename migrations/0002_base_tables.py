# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 06:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blood_donors', '0001_add_sezioni'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroDiRaccolta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=255)),
                ('indirizzo', models.CharField(blank=True, max_length=255)),
                ('frazione', models.CharField(blank=True, max_length=255)),
                ('cap', models.CharField(blank=True, max_length=10)),
                ('citta', models.CharField(blank=True, max_length=255)),
                ('provincia', models.CharField(blank=True, max_length=100)),
                ('tel', models.CharField(blank=True, max_length=255)),
                ('fax', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CentriDiRaccolta',
            },
        ),
        migrations.CreateModel(
            name='Sesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=255, unique=True)),
                ('gg_da_sangue_a_sangue', models.IntegerField()),
                ('gg_da_sangue_a_plasma', models.IntegerField()),
                ('gg_da_sangue_a_piastrine', models.IntegerField()),
                ('gg_da_plasma_a_sangue', models.IntegerField()),
                ('gg_da_plasma_a_plasma', models.IntegerField()),
                ('gg_da_plasma_a_piastrine', models.IntegerField()),
                ('gg_da_piastrine_a_sangue', models.IntegerField()),
                ('gg_da_piastrine_a_plasma', models.IntegerField()),
                ('gg_da_piastrine_a_piastrine', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Sessi',
            },
        ),
        migrations.CreateModel(
            name='StatoDonatore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=255, unique=True)),
                ('descrizione_estesa', models.CharField(max_length=255, unique=True)),
                ('is_attivo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'StatiDonatore',
            },
        ),
        migrations.CreateModel(
            name='TipoDonazione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'TipiDonazione',
            },
        ),
        migrations.AlterUniqueTogether(
            name='centrodiraccolta',
            unique_together=set([('owner', 'descrizione')]),
        ),
    ]
