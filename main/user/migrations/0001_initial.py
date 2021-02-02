# Generated by Django 3.0.7 on 2020-06-12 06:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('lgbt', 'LBGT')], default='male', max_length=20)),
                ('birthdate', models.DateTimeField(auto_now_add=True)),
                ('semester', models.CharField(choices=[('1', '1st'), ('2', '2st'), ('3', '3st'), ('4', '4st'), ('5', '5st'), ('6', '6st'), ('7', '7st'), ('8', '8st')], default='1', max_length=20)),
                ('department', models.CharField(choices=[('comp', 'COMPUTER ENGINEERING'), ('mech', 'MECHANICAL ENGINEERING'), ('ele', 'ELECTRICAL ENGINEERING'), ('civil', 'CIVIL ENGINEERING')], default='comp', max_length=20)),
                ('enrollment', models.CharField(max_length=50)),
                ('lastsemspi', models.CharField(max_length=20)),
                ('lastsemcpi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PreviousMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spi', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=8)),
                ('cpi', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Students')),
            ],
        ),
    ]