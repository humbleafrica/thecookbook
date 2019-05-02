# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-02 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=4000)),
                ('serves', models.IntegerField()),
                ('prep_time', models.DurationField(verbose_name='Preparation Time')),
                ('cook_time', models.DurationField(verbose_name='Cooking Time')),
                ('ingredients', models.TextField(max_length=1500)),
                ('instructions', models.TextField(max_length=15000)),
                ('suits', models.CharField(max_length=1500)),
                ('calories', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('fat', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('saturates', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('carbs', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('sugars', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('fibre', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('protein', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('salt', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('publisher', models.CharField(choices=[('MAG', 'Magazine'), ('WEB', 'Website'), ('BOO', 'Book'), ('SOC', 'Social Club'), ('PRO', 'Professional')], max_length=3, verbose_name='publisher')),
                ('allergy', models.CharField(choices=[('MIL', 'Milk'), ('EGG', 'Egg'), ('NUT', 'Nut'), ('SOY', 'Soya'), ('WHE', 'Wheat'), ('FIS', 'Fish')], max_length=3, verbose_name='allergy')),
                ('difficulty', models.CharField(choices=[('EAS', 'EASY'), ('NOR', 'NORMAL'), ('HAR', 'HARD'), ('EXP', 'EXPERT')], max_length=3, verbose_name='difficulty')),
                ('recipe_type', models.CharField(choices=[('BRE', 'Breakfast'), ('LUN', 'Lunch'), ('DIN', 'Dinner'), ('STA', 'Starter'), ('DES', 'Dessert'), ('STA', 'Starter'), ('BRU', 'Brunch'), ('SNA', 'Snack'), ('MAI', 'Main Course'), ('SID', 'Side Dish'), ('DRI', 'Drink'), ('COC', 'Cocktail'), ('CAN', 'Canape')], max_length=3, verbose_name='recipe Type')),
                ('cuisine', models.CharField(choices=[('AFRICAN', 'African'), ('AMERICAN', 'American'), ('ASIAN', 'Asian'), ('AUSTRALIAN', 'Australian'), ('CARIBBEAN', 'Caribbean'), ('EUROPEAN', 'European'), ('MEDITERRANEAN', 'Mediterranean')], max_length=20, verbose_name='cuisine')),
                ('published_date', models.DateField(blank=True, verbose_name='Date Published')),
                ('uploaded_date', models.DateField(blank=True, verbose_name='Date Uploaded')),
                ('update', models.DateField(blank=True, verbose_name='Last Updated')),
                ('image', models.ImageField(upload_to=b'')),
                ('comments', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'recipe',
                'verbose_name_plural': 'recipes',
            },
        ),
    ]
