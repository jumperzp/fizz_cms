#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='articles')
    title = models.CharField(max_length=100, default='NEW ARTICLE')
    content = models.TextField(blank=True)

    class Meta:
        ordering = ('-created', )
