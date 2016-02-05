# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobrun_profiling_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
