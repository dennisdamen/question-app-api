# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='subject',
            name='next_action',
            field=models.ForeignKey(related_name='next_actions', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
