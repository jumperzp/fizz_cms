#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework import permissions
from cms.models import Article
from cms.serializers import ArticleSerializer
from cms.permissions import IsOwnerOrReadOnly


class AritcleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, )
