#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from cms.models import Article
from cms.serializers import ArticleSerializer, TinyArticleSerializer
from cms.serializers import UserSerializer
from cms.permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class AritcleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TinyArticleSerializer
        return ArticleSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
