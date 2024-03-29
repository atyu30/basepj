#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from django.db.models import permalink

from .fields import ThumbnailImageField

class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
        
    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'pk': self.id})

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)
        
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'pk': self.id})

from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name
