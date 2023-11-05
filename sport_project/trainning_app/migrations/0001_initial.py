# Generated by Django 4.2.5 on 2023-11-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodySize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата')),
                ('biceps', models.PositiveIntegerField(blank=True, null=True, verbose_name='Обхват бицепса')),
                ('breast', models.PositiveIntegerField(blank=True, null=True, verbose_name='Обхват груди')),
                ('waist', models.PositiveIntegerField(blank=True, null=True, verbose_name='Обхват талии')),
                ('buttocks', models.PositiveIntegerField(blank=True, null=True, verbose_name='Обхват ягодиц')),
                ('hip', models.PositiveIntegerField(blank=True, null=True, verbose_name='Обхват бедра')),
            ],
        ),
    ]
