# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dsuser(models.Model):
    objects = models.Manager()
    uid = models.CharField(max_length=128, verbose_name='아이디')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length=100, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='가입일')

    def __str__(self):
        return self.uid, self.password

    class Meta:
        db_table = 'ds_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
