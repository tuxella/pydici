# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0013_auto_20180909_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billexpense',
            name='expense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='expense.Expense', verbose_name='Expense'),
        ),
    ]
