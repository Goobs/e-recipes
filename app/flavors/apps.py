# -*- coding: utf-8 -*-
from django.apps import AppConfig


class PageConfig(AppConfig):
    name = 'app.flavors'
    label = 'flavors'

    def ready(self):
        # from .signals import *
        pass
