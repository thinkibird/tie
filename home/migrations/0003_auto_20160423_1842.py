# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160412_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ForeignKey(blank='True', to='home.Image', null='True'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='founder',
            name='about',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='hospitality',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='hospitality',
            name='image',
            field=models.ForeignKey(blank='True', to='home.Image', null='True'),
        ),
        migrations.AlterField(
            model_name='key_service',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='key_service',
            name='image',
            field=models.ForeignKey(blank='True', to='home.Image', null='True'),
        ),
        migrations.AlterField(
            model_name='our_service',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='our_service',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='our_team',
            name='about',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ForeignKey(blank='True', to='home.Image', null='True'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='review',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
