# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Reviews,Profiles,Projects
from django.contrib import admin


# Register your models here.
admin.site.register(Reviews)
admin.site.register(Profiles)
admin.site.register(Projects)
