# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20151112_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='before',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnails', blank=True, null=True, editable=False),
        ),
    ]
