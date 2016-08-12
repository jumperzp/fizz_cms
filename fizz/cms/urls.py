#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from cms import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'articles', views.AritcleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]