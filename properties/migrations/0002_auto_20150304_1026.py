# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '__first__'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='test',
        ),
        migrations.AddField(
            model_name='property',
            name='address',
            field=address.models.AddressField(blank=True, to='address.Address', null=True),
            preserve_default=True,
        ),
    ]
