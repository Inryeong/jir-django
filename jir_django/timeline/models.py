# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    writer = models.ForeignKey('dsuser.Dsuser', on_delete=models.CASCADE, verbose_name='작성자')
    image_url = models.CharField(max_length=1000, verbose_name='이미지 주소')
    contents = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')

    def __str__(self):
        return self.contents

    class Meta:
        db_table = 'ds_post'
        verbose_name = '포스트'
        verbose_name_plural = '포스트'
