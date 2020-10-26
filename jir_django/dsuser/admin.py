# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Dsuser

# Register your models here.
class DsuserAdmin(admin.ModelAdmin):
    list_display = ('uid', 'password', )

admin.site.register(Dsuser, DsuserAdmin)