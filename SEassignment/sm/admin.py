from django.contrib import admin

from .models import Functions,Goods,Records

class FunctionsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Functions',               {'fields': ['functions_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('functions_text', 'pub_date', 'was_published_recently')
  
  

admin.site.register(Functions,FunctionsAdmin)

class GoodsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Code',                   {'fields': ['code']}),
        ('Price',                  {'fields': ['price']}),
        ('Number',                 {'fields': ['number']}),
    ]
    
  
  

admin.site.register(Goods,GoodsAdmin)


class RecordsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Code',                   {'fields': ['code']}),
        ('Number',                 {'fields': ['number']}),
        ('Total',                  {'fields': ['total']}),
        
    ]
    readonly_fields=('pub_date',)

  

admin.site.register(Records,RecordsAdmin)



