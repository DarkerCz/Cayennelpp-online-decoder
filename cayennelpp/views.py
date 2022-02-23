# -*- coding: UTF-8 -*-

from django.views import generic
from django.utils.translation import ugettext_lazy as _

import logging
logger = logging.getLogger(__name__)

# Dashboard
class IndexView(generic.TemplateView):
    template_name = 'cayennelpp/index.html'