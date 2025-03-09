from django import forms

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea) 
    email = forms.EmailField(help_text="email taak saalya",required=False)  

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 


# SHIFTS = (("1","dagdsfvdf"),("2","sdzfvdv"),("3","sdfgvzdvds"))


# class LogForm(forms.Form):
#     fn= forms.CharField(max_length=200,required=False)
#     ln= forms.CharField(max_length=200)
#     shift = forms.ChoiceField(choices=SHIFTS)

from Home.models import * 

class LogForm(forms.ModelForm):
    class meta:
        model=Logger
        fields='__all__'
    