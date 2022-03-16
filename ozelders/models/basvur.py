from django.db import models
from ozelders.models import IlanlarModel
from account.models import Teacher

class BasvurModel(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,verbose_name="Eğitmen",related_name="basvuru")
    ilan = models.ForeignKey(IlanlarModel, on_delete=models.CASCADE, related_name="basvurular")
    ilan_basvur = models.TextField(verbose_name="Tanıtım Yazısı")
    basvur_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Başvuru Tarihi")

    class Meta:
        db_table ="basvuru"
        verbose_name = "Başvuru"
        verbose_name_plural = "Başvurular"
        ordering = ['basvur_tarihi']

    def __str__(self):
        return self.teacher.username

    
        