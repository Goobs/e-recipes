# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Manufacturer(models.Model):
    name = models.CharField(max_length=75, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)

    class Meta:
        verbose_name = _('manufacturer')
        verbose_name_plural = _('manufacturers')

    def __unicode__(self):
        return self.name


class Flavor(models.Model):
    name = models.CharField(max_length=75, verbose_name=_('name'))
    sku = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('sku'))
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, related_name='flavors',
                                     verbose_name=_('manufacturer'))

    class Meta:
        verbose_name = _('flavor')
        verbose_name_plural = _('flavors')

    def __unicode__(self):
        return self.name


class Review(models.Model):
    flavor = models.ForeignKey(Flavor, related_name='reviews', verbose_name=_('flavor'))
    author_name = models.CharField(max_length=50, blank=True, null=True,
                                   verbose_name=_('author name'))
    content = models.TextField(blank=True, null=True, verbose_name=_('content'))
    favorite_percentage = models.FloatField(blank=True, null=True,
                                            verbose_name=_('favorite percentage'))

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
