from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('decode', views.DecodeView.as_view(), name='decode'),
]