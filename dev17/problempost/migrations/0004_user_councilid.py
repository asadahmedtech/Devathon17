# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problempost', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='councilID',
            field=models.CharField(max_length=10, default=None, choices=[('AC', 'AC'), ('HK', 'HK')]),
            preserve_default=True,
        ),
    ]
