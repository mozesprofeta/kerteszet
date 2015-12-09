# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20151112_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='after',
            old_name='beforephoto',
            new_name='before',
        ),
    ]
