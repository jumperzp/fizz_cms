#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from cms.models import Article


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', )


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')
    content = serializers.HyperlinkedIdentityField(view_name='article-content',
                                                   format='json')

    class Meta:
        model = Article
        fields = ('url', 'pk', 'created', 'author', 'title', 'subtitle', 'content', )