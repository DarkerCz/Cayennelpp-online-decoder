# -*- coding: UTF-8 -*-

from django.views import generic
from django.utils.translation import ugettext_lazy as _

from . import forms

import logging
logger = logging.getLogger(__name__)

# Dashboard
class IndexView(generic.TemplateView):
    template_name = 'cayenne_decoder/index.html'

class DecodeView(generic.FormView):
    template_name = 'cayenne_decoder/decode.html'
    form_class = forms.DecodeForm