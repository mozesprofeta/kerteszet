# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_after_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='after',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnails', blank=True, editable=False),
        ),
    ]
