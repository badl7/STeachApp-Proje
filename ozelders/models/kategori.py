from django.db import models
from autoslug import AutoSlugField
from account.models import Teacher

class KategoriModel(models.Model):
    ders = models.CharField(max_length=150, blank=False, null=False)
    slug = AutoSlugField(populate_from="ders")
    
    class Meta:
        db_table = 'kategori'
        verbose_name_plural = "Kategoriler"
        verbose_name = "Kategori"
    def __str__(self):
        return self.ders


        