# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problempost', '0006_auto_20170902_0116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='profile',
        ),
    ]
