# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-08 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipe_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='allergy',
            field=models.CharField(choices=[('NONE', 'NONE'), ('MILK', 'MILK'), ('EGG', 'EGG'), ('NUT', 'NUT'), ('SOYA', 'SOYA'), ('WHEAT', 'WHEAT'), ('FISH', 'FISH'), ('PORK', 'PORK')], max_length=20, verbose_name='allergy'),
        ),
    ]
