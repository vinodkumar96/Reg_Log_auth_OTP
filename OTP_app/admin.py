from django.contrib import admin
from  . models import Reg
# Register your models here.
class Reg_admin (admin.ModelAdmin):
    list_display = ['f_name','l_name','dob','mob_no','email','u_name','p_word']
    list_filter = ['dob']
    class meta:
        model =Reg
admin.site.register(Reg,Reg_admin)
