# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SubscriberUser


class SubscriberUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'is_follow', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = (
        ('username', 'email'), ('first_name', 'last_name'),
        ('is_staff', 'is_superuser'), 'groups', 'user_permissions',
        ('last_login', 'date_joined')
    )
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(SubscriberUser, SubscriberUserAdmin)
