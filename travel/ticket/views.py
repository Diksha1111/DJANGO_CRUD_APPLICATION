from django.shortcuts import render,redirect
from . models import Member

# Create your views here.
def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['name']
    y=request.POST['age']
    z=request.POST['nationality']
    a=request.POST['gender']
    b=request.POST['trainName']
    c=request.POST['berth']
    d=request.POST['classs']
    e=request.POST['fromm']
    f=request.POST['to']
    mem=Member(name=x,age=y,nationality=z,gender=a,trainName=b,berth=c,classs=d,fromm=e,to=f)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem= Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem= Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})


def uprec(request,id):
    x=request.POST['name']
    y=request.POST['age']
    z=request.POST['nationality']
    a=request.POST['gender']
    b=request.POST['trainName']
    c=request.POST['berth']
    d=request.POST['classs']
    e=request.POST['fromm']
    f=request.POST['to']
    
    mem=Member.objects.get(id=id)
    mem.name=x
    mem.age=y
    mem.nationality=z
    mem.gender=a
    mem.trainName=b
    mem.berth=c
    mem.classs=d
    mem.fromm=e
    mem.to=f
    mem.save()
    return redirect("/")   


