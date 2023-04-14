from django.contrib import admin
from . models import  Civilservants, Retirement, Reports

# Register your models here.

class CivilservantsAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "gender", "ministry", "department", "marital_status", "date_of_birth", "phone", "email", "address", "appointment_date"]
    search_fields = ["firstname", "lastname", "department", "phone"]
    list_per_page = 10

admin.site.register(Civilservants, CivilservantsAdmin)  

class RetirementAdmin(admin.ModelAdmin):
    list_filter = ['retirement_status']
    list_display = ["retiree_name", "retiree_ministry", "retiree_department", "dob", "appointment_date", "age", "years_of_work", "retirement_status"]
    search_fields = ["retiree_name", "retiree_ministry", "retiree_department"]
    list_per_page = 10

admin.site.register(Retirement, RetirementAdmin) 

class ReportsAdmin(admin.ModelAdmin):
    list_display = ["Retname", "Minist", "Dept", "Apt_date", "Dob", "Age", "Duration", "Status"]
    search_fields = ["Retname", "status"]
    list_per_page = 10

admin.site.register(Reports, ReportsAdmin)  
