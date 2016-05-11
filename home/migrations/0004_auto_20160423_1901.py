# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160423_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null='True', upload_to='SETTINGS.MEDIA_URL.img', blank='True'),
        ),
    ]
