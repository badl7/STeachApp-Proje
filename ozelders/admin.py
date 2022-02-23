from django.contrib import admin
from ozelders.models import KategoriModel,IlanlarModel


admin.site.register(KategoriModel)


class IlanlarAdmin(admin.ModelAdmin):
    list_display = ["ilan_baslik","ilan_sahibi","olus_tarih","konum"]
    list_display_links = ["ilan_baslik","ilan_sahibi"]
    search_fields = ["ilan_baslik"] 
    

admin.site.register(IlanlarModel,IlanlarAdmin)
