# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('build_id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('build_date', models.DateTimeField()),
                ('target_machine', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='BuildDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repository', models.CharField(max_length=128)),
                ('revision', models.CharField(max_length=64)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Build')),
            ],
        ),
        migrations.CreateModel(
            name='Sstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artifact_type', models.CharField(choices=[('target', 'Target artifact'), ('native', 'Native artifact')], max_length=16)),
                ('rb_status', models.CharField(max_length=1)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Build')),
            ],
        ),
        migrations.CreateModel(
            name='SstateTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=128)),
                ('diff', models.BinaryField()),
                ('sstate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Sstate')),
            ],
        ),
    ]