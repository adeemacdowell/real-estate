# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.utils import timezone
from authweb.realestate.demo import demo_mode


class Entry(models.Model):
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    square_feet = models.IntegerField(default=0)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    agency = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    price = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/real-estate/')

    @property
    def get_image_path(self):
        from authweb.config.settings.base import MEDIA_URL
        from authweb.realestate.demo import default_demo_images
        if demo_mode and self.image in default_demo_images:
            return self.image
        return "{}{}".format(MEDIA_URL, self.image)

    @staticmethod
    def get_entries():
        entries = Entry.objects.all()
        if entries:
            entries = entries.order_by('-id')
            if demo_mode:
                entries = entries.order_by('-id')[:5]

            for i, entry in enumerate(entries, start=1):
                entry.image = entry.get_image_path
                entry.css_size = "col-lg-8" if i == 1 else "col-sm-6 col-lg-4"
            return entries

        return entries