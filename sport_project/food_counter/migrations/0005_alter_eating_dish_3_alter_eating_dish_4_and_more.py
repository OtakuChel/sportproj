# Generated by Django 4.2.5 on 2023-10-29 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_counter', '0004_remove_eatingdate_day_remove_eatingdate_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eating',
            name='dish_3',
            field=models.CharField(blank=True, max_length=20, verbose_name='Блюдо №3'),
        ),
        migrations.AlterField(
            model_name='eating',
            name='dish_4',
            field=models.CharField(blank=True, max_length=20, verbose_name='Блюдо №4'),
        ),
        migrations.AlterField(
            model_name='eating',
            name='dish_5',
            field=models.CharField(blank=True, max_length=20, verbose_name='Блюдо №5'),
        ),
        migrations.AlterField(
            model_name='eating',
            name='dish_6',
            field=models.CharField(blank=True, max_length=20, verbose_name='Блюдо №6'),
        ),
        migrations.AlterField(
            model_name='eating',
            name='weight_2',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Граммовка блюда №2'),
        ),
        migrations.AlterField(
            model_name='eating',
            name='weight_3',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Граммовка блюда №3'),
        ),
        migrations.AlterField(
            model_name='eating',
            name='weight_4',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Граммовка блюда №4'),
        ),
        migrations.AlterField(
            model_name='eating',
            name='weight_5',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Граммовка блюда №5'),
        ),
        migrations.AlterField(
            model_name='eating',
            name='weight_6',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Граммовка блюда №6'),
        ),
    ]
