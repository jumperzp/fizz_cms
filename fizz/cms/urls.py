#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from cms import views

router = DefaultRouter()
router.register(r'article', views.AritcleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]