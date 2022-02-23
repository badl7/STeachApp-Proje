from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    ders = models.CharField(max_length=150, blank=False, null=False)
    slug = AutoSlugField(populate_from="ders")
    