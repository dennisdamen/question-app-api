# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lastEdited', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lastEdited', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(related_name='subjects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-lastEdited',),
            },
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(related_name='questions', to='questions.Subject'),
        ),
    ]
