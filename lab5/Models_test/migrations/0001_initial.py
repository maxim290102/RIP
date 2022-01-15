# Generated by Django 3.2.9 on 2021-12-04 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('colour', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Models_test.customer')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]