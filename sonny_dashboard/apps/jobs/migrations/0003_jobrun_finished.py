# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150820_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrun',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
