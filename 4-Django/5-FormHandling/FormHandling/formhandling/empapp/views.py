from django.shortcuts import render
from . import forms

# Create your views here.
def regform(r):
    form=forms.EmpInfo()
    if r.method=='POST':
        form=forms.EmpInfo(r.POST)
        msg='We have recieved this form again'
        if form.is_valid():
            msg=msg+' Form is valid '
    else:
        msg='Welcome to first time !'
    return render(r,'index.html',{'form':form,'msg':msg})
