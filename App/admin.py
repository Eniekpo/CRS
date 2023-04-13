from django.contrib import admin
from . models import  Civilservants, csdetails, Retirement, Reports

# Register your models here.

class CivilservantsAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "gender", "ministry", "department", "marital_status", "date_of_birth", "phone", "email", "address", "appointment_date"]
    search_fields = ["firstname", "lastname", "department", "phone"]
    list_per_page = 10

admin.site.register(Civilservants, CivilservantsAdmin)  

class csdetailsAdmin(admin.ModelAdmin):
    list_display = ["name", "minist", "dept", "cs_age", "cs_years"]
    search_fields = ["name", "dept"]
    list_per_page = 10

admin.site.register(csdetails, csdetailsAdmin)  

class RetirementAdmin(admin.ModelAdmin):
    list_display = ["retiree_name", "dob", "appointment_date", "age", "years_of_work", "retirement_status"]
    search_fields = ["retiree_name", "dob"]
    list_per_page = 10

admin.site.register(Retirement, RetirementAdmin) 

class ReportsAdmin(admin.ModelAdmin):
    list_display = ["Retname", "Minist", "Dept", "Apt_date", "Dob", "Age", "Duration", "Status"]
    search_fields = ["Retname", "status"]
    list_per_page = 10

admin.site.register(Reports, ReportsAdmin)  
