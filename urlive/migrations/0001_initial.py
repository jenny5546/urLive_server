# Generated by Django 2.1.11 on 2019-11-03 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=64, unique=True)),
                ('pincode', models.CharField(default='null', max_length=8, unique=True)),
                ('encrypt', models.CharField(default='null', max_length=20, unique=True)),
                ('is_selected', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='null', max_length=5)),
                ('uid', models.TextField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urlive.Room')),
            ],
        ),
    ]
