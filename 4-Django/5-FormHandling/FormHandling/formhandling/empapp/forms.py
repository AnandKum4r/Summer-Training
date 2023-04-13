from django import forms

def check_size(value):
    if len(value)<8:
        raise forms.ValidationError('The Password is too short')
class EmpInfo(forms.Form):
    empid=forms.IntegerField()
    empname=forms.CharField()
    address=forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Address'}))
    contactno=forms.CharField()
    emailaddress= forms.EmailField(help_text='Enter your Email')
    password=forms.CharField(widget=forms.PasswordInput,validators=[check_size])
    confirmpassword=forms.CharField(help_text='Confirm password',widget=forms.PasswordInput)
