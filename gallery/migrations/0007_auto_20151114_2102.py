# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20151114_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='after',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='before',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
