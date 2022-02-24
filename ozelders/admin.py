from django.contrib import admin
from ozelders.models import KategoriModel,IlanlarModel,BasvurModel,IletisimModel


admin.site.register(KategoriModel)

@admin.register(IlanlarModel)
class IlanlarAdmin(admin.ModelAdmin):
    list_display = ["ilan_baslik","ilan_sahibi","olus_tarih","konum"]
    list_display_links = ["ilan_baslik","ilan_sahibi"]
    search_fields = ["ilan_baslik"] 

@admin.register(BasvurModel)
class BasvurAdmin(admin.ModelAdmin):
    list_display = ["teacher","ilan"]
    list_display_links = ["ilan","teacher"]
    search_fields = ["teacher__username"] #teacher'ı user'dan kullandığımız için


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = ('email', 'olusturulma_tarihi')
    search_fields = ('email',)