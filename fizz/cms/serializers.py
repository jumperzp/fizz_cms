#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from cms.models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Article
        fields = ('url', 'pk', 'created', 'title', 'subtitle', 'content')