from django.shortcuts import render, redirect
from . models import Student

# Create your views here.
def index(request):
    users=Student.objects.all()
    con={'users':users}
    return render(request,'index.html',con)

def register(request):
    return render(request,'register.html')
def save(request):
    n=request.POST['name']
    a=request.POST['address']
    c=request.POST['contactno']
    e=request.POST['emailaddress']
    user=Student(name=n,address=a,contactno=c,emailaddress=e)
    user.save()
    return redirect('index')



