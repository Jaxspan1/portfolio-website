# Generated by Django 3.0.2 on 2020-07-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200714_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
