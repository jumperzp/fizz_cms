#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import viewsets
from cms.models import Article
from cms.serializers import ArticleSerializer


class AritcleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer