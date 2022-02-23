from atexit import register
from django.contrib import admin
from ozelders.models import KategoriModel,IlanlarModel


admin.site.register(KategoriModel)

@admin.register(IlanlarModel)
class IlanlarAdmin(admin.ModelAdmin):
    list_display = ["ilan_baslik","ilan_sahibi","olus_tarih","konum"]
    list_display_links = ["ilan_baslik","ilan_sahibi"]
    search_fields = ["ilan_baslik","ilan_sahibi"] 
    list_filter = ["olus_tarih"]

    class Meta:
        model = IlanlarModel