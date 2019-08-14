from django import forms
from . models import Reg
class Reg_form (forms.ModelForm):
    class Meta:
        model = Reg
        widgets = {'p_word':forms.PasswordInput(),'cp_word':forms.PasswordInput()}
        fields = ['f_name','l_name','dob','mob_no','email','u_name','p_word','cp_word']

class Log_form (forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
