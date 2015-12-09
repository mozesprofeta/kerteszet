# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_before_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='after',
            name='thumbnail',
            field=models.ImageField(editable=False, null=True, upload_to='thumbnail', blank=True),
        ),
    ]
