# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_jobrun_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrun',
            name='profiling_json',
            field=models.TextField(null=True),
        ),
    ]
