# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditionaloffer',
            name='name',
            field=models.CharField(help_text="This is displayed within the customer's basket", max_length=128, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conditionaloffer',
            name='slug',
            field=oscar.models.fields.autoslugfield.AutoSlugField(populate_from=b'name', verbose_name='Slug', max_length=128, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='range',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='range',
            name='slug',
            field=oscar.models.fields.autoslugfield.AutoSlugField(populate_from=b'name', verbose_name='Slug', max_length=128, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
