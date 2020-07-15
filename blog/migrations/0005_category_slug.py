# Generated by Django 3.0.2 on 2020-07-14 15:28

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='django', editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]