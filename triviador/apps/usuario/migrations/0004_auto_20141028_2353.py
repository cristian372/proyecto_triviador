# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'img_user'),
        ),
    ]
