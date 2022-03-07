# -*- coding: UTF-8 -*-

from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse

from . import forms
from . import utils
from . import settings as app_settings

import logging
logger = logging.getLogger(__name__)

# Dashboard
class IndexView(generic.TemplateView):
    template_name = 'cayenne_decoder/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GOOGLE_ANALYTICS'] = getattr(app_settings, "GOOGLE_ANALYTICS", "ID-GOOGLE-ANALYTICS")
        return context


class DecodeView(generic.FormView):
    template_name = 'cayenne_decoder/decode.html'
    form_class = forms.DecodeForm

    def form_valid(self, form):
        data = form.cleaned_data['decode_text']
        logger.debug(utils.process_decoding(data))
        decoded_data = utils.process_decoding(data)
        return JsonResponse({'success': True, 'decoded_data': decoded_data}, status=200)
        return JsonResponse({'success': False}, status=400)