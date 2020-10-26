# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='태그명')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일자')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ds_tag'
        verbose_name = '태그'
        verbose_name_plural = '태그'
