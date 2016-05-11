# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('title', models.CharField(max_length=15)),
                ('overview', models.TextField(max_length=250, blank='True')),
                ('description', models.TextField(max_length=500)),
                ('position', models.IntegerField(serialize=False, primary_key='True')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand', models.CharField(max_length=15)),
                ('overview', models.TextField(max_length=250, blank='True')),
                ('description', models.TextField(max_length=500)),
                ('position', models.IntegerField(serialize=False, primary_key='True')),
                ('website', models.URLField(blank='True')),
                ('fblink', models.URLField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(to='contactus.Address')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null='False')),
                ('designation', models.CharField(max_length=30, null='False')),
                ('about', models.TextField(max_length=500, blank='True')),
                ('position', models.IntegerField(null='False', blank='False')),
                ('fblink', models.URLField(blank='False')),
                ('twlink', models.URLField(blank='False')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Hospitality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=15, null='False', blank='False')),
                ('description', models.TextField(max_length=500)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_alt', models.CharField(max_length=30, blank='False')),
                ('image_title', models.CharField(max_length=30, blank='False')),
                ('image', models.ImageField(height_field='height_field', width_field='width_field', null='True', upload_to='SETTINGS.MEDIA_URL.img', blank='True')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Key_Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=15, null='False', blank='False')),
                ('description', models.TextField(max_length=500)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.ForeignKey(to='home.Image')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Our_Service',
            fields=[
                ('title', models.CharField(max_length=15)),
                ('overview', models.TextField(max_length=250, blank='True')),
                ('description', models.TextField(max_length=500)),
                ('position', models.IntegerField(serialize=False, primary_key='True')),
                ('image', models.ForeignKey(to='home.Image', blank='True')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Our_team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null='False')),
                ('designation', models.CharField(max_length=30, null='False')),
                ('about', models.TextField(max_length=500, blank='True')),
                ('position', models.IntegerField(null='False', blank='False')),
                ('fblink', models.URLField(blank='False')),
                ('twlink', models.URLField(blank='False')),
                ('team_image', models.ForeignKey(to='home.Image')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null='False')),
                ('review', models.TextField(max_length=250)),
                ('rating', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image', models.ForeignKey(to='home.Image', null='False')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.AddField(
            model_name='hospitality',
            name='image',
            field=models.ForeignKey(to='home.Image'),
        ),
        migrations.AddField(
            model_name='founder',
            name='founder_image',
            field=models.ForeignKey(to='home.Image'),
        ),
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ForeignKey(to='home.Image', blank='True'),
        ),
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ForeignKey(related_name='About_Image', to='home.Image'),
        ),
    ]
