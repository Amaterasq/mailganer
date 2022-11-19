# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser

from django.db import models


class SubscriberUser(AbstractUser):
    is_follow = models.BooleanField(
        default=True,
        verbose_name='is follow?'
    )

    class Meta(AbstractUser.Meta):
        pass
