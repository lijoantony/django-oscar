# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oscar.models.fields.autoslugfield
import oscar.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='upc',
            field=oscar.models.fields.NullCharField(help_text='Universal Product Code (UPC) is an identifier for a product which is not specific to a particular  supplier. Eg an ISBN for a book.', max_length=64, verbose_name='UPC'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productclass',
            name='slug',
            field=oscar.models.fields.autoslugfield.AutoSlugField(populate_from=b'name', verbose_name='Slug', max_length=128, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
