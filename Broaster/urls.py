# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""Broaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
#from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.home',name="home"),
    url(r'^about-us$', 'home.views.about',name="about"),
    url(r'^brands$', 'home.views.brand',name="brand"),
    url(r'^services$', 'home.views.our_service',name="our_service"),
    url(r'^contact$', 'contactus.views.contactus', name="contact"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls'),name='upload-image'),
    ]
urlpatterns += staticfiles_urlpatterns()
"""if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""