from django.contrib import admin
from .models import (
    Novinky, 
    Oznamy, 
    UradnaTabula, 
    Odpad, 
    Aktuality, 
    Vzn, 
    FakturyRok, 
    FakturyFiles,
    ZmluvyRok,
    ZmluvyFiles,
    ZapisniceObdobie,
    ZapisniceFiles,
    )

class FakturyFilesInline(admin.TabularInline):
    model = FakturyFiles

class FakturyRokAdmin(admin.ModelAdmin):
    inlines = [FakturyFilesInline,]
    list_display = ('rok', "title", 'faktura')

class ZmluvyFilesInline(admin.TabularInline):
    model = ZmluvyFiles

class ZmluvyRokAdmin(admin.ModelAdmin):
    inlines = [ZmluvyFilesInline,]
    list_display = ('rok', "title", 'zmluva')

class ZapisniceFilesInline(admin.TabularInline):
    model = ZapisniceFiles

class ZapisniceObdobieAdmin(admin.ModelAdmin):
    inlines = [ZapisniceFilesInline,]
    list_display = ('obdobie', "typ", 'date', 'zapisnica', 'uznesenie')

# Register your models here.
admin.site.register(Novinky)
admin.site.register(Oznamy)
admin.site.register(UradnaTabula)
admin.site.register(Odpad)
admin.site.register(Aktuality)
admin.site.register(Vzn)
admin.site.register(FakturyRok)
admin.site.register(FakturyFiles)
admin.site.register(ZmluvyRok)
admin.site.register(ZmluvyFiles)
admin.site.register(ZapisniceObdobie)
admin.site.register(ZapisniceFiles)