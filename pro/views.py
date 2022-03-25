
from django.shortcuts import render
from .forms import contact_me
from .models import contact
# Create your views here.
def home(request):
    return render(request,'home.html')
    
def index(request):
    return render(request,'index.html')
def Contact(request):
    return render(request,'contact.html')

def showcontact(request):
    if request.method=='POST':
        contact=contact_me(request.POST)
        if contact.is_valid():
           name = request.POST.get('Name')
           email = request.POST.get('Email_Address')
           txt = request.POST.get('Text')
           contact.Name=name
           contact.Email_Address=email
           contact.Text=txt
           contact.save()
    else:
         contact=contact_me()
    return render(request,'pro/contacte.html',{'form':contact})

def show(request):
    data=contact.objects.all()
    for i in data:
        print(i)
    return render(request,'showdata.html',{'contact':data})