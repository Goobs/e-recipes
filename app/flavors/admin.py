# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *


class ManufacturerAdmin(admin.ModelAdmin):
    pass


class FlavorAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(Review, ReviewAdmin)
