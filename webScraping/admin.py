from django.contrib import admin
from webScraping.models import company_details
from webScraping.models import company_other_info
# Register your models here.
# class CompanyDetailsAdmin(admin.ModelAdmin):
#     list_display = ('CompanyName','TradingCode','ScripCode','Sector')
# class CompanyOtherInfoAdmin(admin.ModelAdmin):
#     list_display = ('TradingCode','Date','SponsorDirector','Govt','Institute','ForeignNum','Public')
admin.site.register(company_details)
admin.site.register(company_other_info)