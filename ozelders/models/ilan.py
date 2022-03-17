from django.db import models
from autoslug import AutoSlugField
from ozelders.models import KategoriModel
from account.models import Student


class IlanlarModel(models.Model):
    ilan_sahibi = models.ForeignKey(Student, related_name="ilanlar", on_delete=models.CASCADE, verbose_name="İlanı Veren")
    ilan_baslik = models.CharField(max_length=50,verbose_name="İlan Başlığı")
    konum = models.CharField(max_length=50,verbose_name="Konum")
    okulu = models.CharField(max_length=150,verbose_name="Eğitim Seviyesi")
    icerik = models.TextField(verbose_name="Detaylar")
    fiyat = models.IntegerField(verbose_name="Ücret")
    olus_tarih = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    slug = AutoSlugField(populate_from="ilan_baslik", unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name = "ilan")
    
    class Meta:
        verbose_name = "İlan"
        verbose_name_plural= "İlanlar"
        db_table = "ilan"
    def __str__(self):
        return self.ilan_baslik
        