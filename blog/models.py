# coding:utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
 
@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100)
    qq = models.CharField(max_length=100)
    addr = models.TextField()
    email = models.EmailField()
    
    class Meta:
        app_label = 'blog'
        verbose_name = u'作者'
        verbose_name_plural = u'作者'
    
#     def __unicode__(self):
#         return self.name
    def __str__(self):
        return self.name

 
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
 
 
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name
