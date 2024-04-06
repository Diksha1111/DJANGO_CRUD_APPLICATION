from django.contrib import admin
from . models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display="name","age","nationality","gender","trainName","berth","classs","fromm","to"
    
admin.site.register(Member, MemberAdmin)