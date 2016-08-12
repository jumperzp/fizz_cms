#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from cms.models import Article
from cms.serializers import ArticleSerializer
from cms.serializers import UserSerializer
from cms.permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class AritcleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @detail_route()
    def content(self, request, *args, **kwargs):
        article = self.get_object()
        return Response(article.content)
