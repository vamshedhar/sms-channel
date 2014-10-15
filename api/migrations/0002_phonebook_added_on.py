# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebook',
            name='added_on',
            field=models.DateField(default=datetime.date(2014, 10, 15), auto_now_add=True),
            preserve_default=False,
        ),
    ]
