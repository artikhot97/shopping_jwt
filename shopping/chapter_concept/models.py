# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# Create your models here.

class Chapter(models.Model):
    chapter_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)
    author = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.chapter_name

    class Meta:
        db_table = 'chapter'

class Concept(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    concept_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.concept_text

    class Meta:
        db_table = 'concept'
