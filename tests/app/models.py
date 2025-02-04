"""
Models for testing wagtailimporter.
"""
from django.db import models
from wagtail import VERSION
if VERSION < (5,0):
    from wagtail.contrib.settings.models import BaseSetting, register_setting
    from wagtail.core.models import Page
else:
    from wagtail.models import Page
    from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


class BasicPage(Page):
    """The simplest page type."""
    body = models.TextField(blank=True)


class ForeignKeyPage(Page):
    """A page with some foreign keys to other things."""
    other_page = models.ForeignKey(
        Page, related_name='+',
        null=True, blank=True, default=None, on_delete=models.SET_NULL)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True, default=None, on_delete=models.SET_NULL)


@register_setting
class BasicSetting(BaseSiteSetting):
    """The simplest setting."""
    text = models.TextField(blank=True)
    cute_dog = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True, default=None, on_delete=models.SET_NULL)
