# -*- coding: UTF-8 -*-

import struct
import json
import base64
import binascii
import datetime

from uuid import uuid4

from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

import logging
logger = logging.getLogger(__name__)


class DataType(TimeStampedModel):

    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)

    type = models.CharField('Type', max_length=128)
    ipso = models.IntegerField('IPSO')
    lpp = models.IntegerField('LPP')
    hex = models.IntegerField('HEX')
    data_size = models.IntegerField('Data Size')

    class Meta:
        verbose_name = 'Data Type'
        verbose_name_plural = 'Data Types'
        ordering = ('hex',)

class Payload(TimeStampedModel):

    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)

    value = models.CharField('Value', max_length=2048)
    counter = models.IntegerField("Counter", default=0)

    class Meta:
        verbose_name = 'Payload'
        verbose_name_plural = 'Payloads'
        ordering = ('-created',)


class Value(TimeStampedModel):

    uuid = models.UUIDField(unique=True, default=uuid4, editable=False)

    payload = models.ForeignKey(Payload, related_name='values', verbose_name='Payload',
        blank=True, null=True, on_delete=models.SET_NULL)

    type = models.ForeignKey(DataType, related_name='values', verbose_name='Type',
        blank=True, null=True, on_delete=models.SET_NULL)
    channel = models.IntegerField('Channel')
    value = models.CharField('Value', max_length=1024) 

    class Meta:
        verbose_name = 'Value'
        verbose_name_plural = 'Values'
        ordering = ('-created',)


