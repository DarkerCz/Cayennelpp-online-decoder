from django.views import generic
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('decode', views.DecodeView.as_view(), name='decode'),
    path("robots.txt", generic.TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
