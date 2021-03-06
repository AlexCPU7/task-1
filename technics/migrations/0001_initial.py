# Generated by Django 2.1.1 on 2018-09-18 19:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Модел')),
                ('max_weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Макс. грузоподъемность')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='Tipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Бортовой номер')),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Текущий вес')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technics.Model', verbose_name='Модел')),
            ],
            options={
                'verbose_name': 'Самосвал',
                'verbose_name_plural': 'Самосвалы',
            },
        ),
    ]
