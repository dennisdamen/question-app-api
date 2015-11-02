# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151102_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='question',
        ),
    ]
