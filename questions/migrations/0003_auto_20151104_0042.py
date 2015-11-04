# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151104_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='next_action',
            field=models.ForeignKey(related_name='next_actions', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
