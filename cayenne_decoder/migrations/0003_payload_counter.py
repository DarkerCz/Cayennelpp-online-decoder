# Generated by Django 3.2.6 on 2022-02-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cayenne_decoder', '0002_value_payload'),
    ]

    operations = [
        migrations.AddField(
            model_name='payload',
            name='counter',
            field=models.IntegerField(default=0, verbose_name='Counter'),
        ),
    ]
