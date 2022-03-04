#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

class DecodeForm(forms.Form):
    decode_text = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['decode_text'].widget.attrs['class'] = 'form-control'
        self.fields['decode_text'].required = True
        self.fields['decode_text'].initial = '03670110056700FF'
