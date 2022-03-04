import json
from math import ceil
import struct
import base64
import binascii
import random

from cayennelpp import LppFrame

from . import models

import logging
logger = logging.getLogger(__name__)

def check_base64(text):
    try:
        return base64.b64decode(text).decode("utf-8")
    except Exception as e:
        return text

def decode(text):
    try:
        buffer = bytearray([int(text[i:i + 2], 16) for i in range(0, len(text), 2)])
        frame = LppFrame().from_bytes(buffer)
        return frame
    except Exception as e:
        logger.warning("Error while decoding text: {}, Error: {}".format(text, e))
        return False


def process_decoding(text):
    text = check_base64(text)
    text = text.upper().replace("0X", "").replace(" ", "")
    try:
        payload = models.Payload.objects.get(value=text)
        payload.counter += 1
        payload.save()
        return list(payload.values.all().order_by('created').values_list('type', 'type__type', 'channel', 'value'))
    except Exception:
        decoded_text = decode(text)
        if decoded_text:
            payload = models.Payload.objects.create(value=text)
            for value in decoded_text:
                datatype = models.DataType.objects.get(lpp=value.type.type)
                models.Value.objects.create(payload=payload, type=datatype, channel=value.channel, value=value.value)
            return list(payload.values.all().order_by('created').values_list('type', 'type__type', 'channel', 'value'))
    return None

