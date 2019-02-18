# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-18 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.IntegerField(verbose_name='id')),
                ('category', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='category')),
                ('hasDamage', models.BooleanField(default=False, verbose_name='hasDamage')),
                ('price', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='price')),
                ('title', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='title')),
                ('created', models.IntegerField(verbose_name='created')),
                ('modified', models.IntegerField(verbose_name='modified')),
                ('renewed', models.IntegerField(verbose_name='renewed')),
                ('features', models.CharField(blank=True, default='', max_length=750, null=True, verbose_name='features')),
                ('details', models.CharField(blank=True, default='', max_length=750, null=True, verbose_name='details')),
                ('attr', models.CharField(blank=True, default='', max_length=750, null=True, verbose_name='attr')),
                ('url', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='url')),
            ],
        ),
    ]
