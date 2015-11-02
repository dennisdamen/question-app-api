# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_remove_subject_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
