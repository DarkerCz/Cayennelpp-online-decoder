#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

class DecodeForm(forms.Form):
    decode_text = forms.CharField()
