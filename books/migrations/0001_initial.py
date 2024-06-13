# Generated by Django 5.0.6 on 2024-06-10 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nomi')),
                ('description', models.TextField(verbose_name='category haqida')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='kitob nomi')),
                ('slug', models.TextField(verbose_name='kitob haqida')),
                ('picture', models.ImageField(upload_to='', verbose_name='rasmi')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='narxi')),
                ('quantitiy', models.IntegerField(verbose_name='qancha bor')),
                ('status', models.CharField(choices=[('sotuvda', 'Sotuvda'), ('qolmagan', 'qolmagan')], max_length=50, verbose_name='holati')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.bookcategory')),
            ],
        ),
    ]
