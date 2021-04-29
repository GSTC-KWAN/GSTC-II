from django.contrib import admin

# Register your models here.
from .models import Platform 

    

class PlatformAdmin(admin.ModelAdmin):
    fieldsets=[
            ('Guidance to application form page',            {'fields':['platform_text']}),
            ('Social Security Number',                       {'fields':['ssn']}),
            ('Name',                                        {'fields':['name']}),
            ('Annual Income ',                       {'fields':['annualincome']}),
            ('Working years ',                       {'fields':['workingyears']}),
            
            ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
            ]

    list_display=('platform_text','pub_date','was_published_recently')
    

admin.site.register(Platform, PlatformAdmin)
