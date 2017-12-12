# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=90)),
                ('gps_weigth', models.DecimalField(max_digits=10, decimal_places=7)),
                ('gps_length', models.DecimalField(max_digits=10, decimal_places=7)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_fish', models.CharField(unique=True, max_length=50)),
                ('psychology', models.TextField(max_length=2000)),
                ('about', models.TextField(max_length=2000)),
                ('start_nerest', models.DateField()),
                ('end_nerest', models.DateField()),
                ('food', models.TextField(max_length=300)),
                ('default_img', models.ImageField(upload_to=b'')),
                ('ico_img', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_water', models.CharField(max_length=6, choices=[(b'lake', b'\xd0\x9e\xd0\xb7\xd0\xb5\xd1\x80\xd0\xbe'), (b'river', b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xb0'), (b'sea', b'\xd0\x9c\xd0\xbe\xd1\x80\xd0\xb5'), (b'mini_lake', b'\xd0\x9f\xd1\x80\xd1\x83\xd0\xb4')])),
                ('name', models.CharField(unique=True, max_length=70)),
                ('behind_city', models.ForeignKey(to='main.City', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ImgFish',
        ),
        migrations.DeleteModel(
            name='ImgOther',
        ),
        migrations.RemoveField(
            model_name='imgtackle',
            name='who_added',
        ),
        migrations.RemoveField(
            model_name='tackle',
            name='img',
        ),
        migrations.DeleteModel(
            name='ImgTackle',
        ),
        migrations.AddField(
            model_name='fish',
            name='home',
            field=models.ManyToManyField(to='main.Water'),
        ),
    ]
