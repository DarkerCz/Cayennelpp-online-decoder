# Generated by Django 3.2.6 on 2022-02-25 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cayenne_decoder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='payload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='values', to='cayenne_decoder.payload', verbose_name='Payload'),
        ),
    ]