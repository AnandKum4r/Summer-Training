from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'aboutus.html')
def contact(request):
    return render(request,'contactus.html')
def register(request):
    return render(request,'register.html')
