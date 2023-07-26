from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from autoapp.models import catdb,productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.
def indexpage(request):
    return render(request,"index.html")
def adminpage(request):
    return render(request,"login.html")

def loginadmin(request):
    if request.method =="POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username']=uname
                request.session['password']=pwd
                messages.success(request, "Login successfull ")
                return redirect(indexpage)

            else:
                messages.error(request, "Invalid username/password ")
                return redirect(adminpage)
        else:
            messages.error(request, "Invalid username/password ")
            return redirect(adminpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfull ")
    return redirect(adminpage)
def catpage(request):
    return render(request,"category.html")
def savecata(request):
    if request.method =="POST":
        cn = request.POST.get('Name')
        cd = request.POST.get('Description')
        cimg = request.FILES['Image']
        obj=catdb(cname=cn,cdes=cd,cimage=cimg)
        obj.save()
        messages.success(request,"category added successfully")
        return redirect(catpage)

def catdisplay(req):
    cdata = catdb.objects.all()
    return render(req,"displaycat.html",{'cdata':cdata})
def catedit(req,catid):
    cat = catdb.objects.get(id=catid)
    return render(req,"editcat.html",{'cat':cat})

def updatecat(req,catid):
    if req.method=="POST":
        na = req.POST.get('Name')
        de = req.POST.get('Description')
        try:
            img = req.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=catid).cimage
        catdb.objects.filter(id=catid).update(cname=na,cdes=de,cimage=file)
        return redirect(catdisplay)
def deletecat(req,catid):
    data=catdb.objects.get(id=catid)
    data.delete()
    return redirect(catdisplay)
def productpage(req):
    cat = catdb.objects.all()
    return render(req,"addproduct.html",{'cat':cat})
def saveproduct(req):
    if req.method== "POST":
        ps = req.POST.get('Select')
        pn = req.POST.get('Name')
        pd = req.POST.get('Des')
        pp = req.POST.get('Price')
        pimg = req.FILES['Image']
        obj = productdb(pselect=ps,pname=pn,pdes=pd,pprice=pp,pimage=pimg)
        obj.save()
        return redirect(productpage)
def productdisplay(req):
    pdata = productdb.objects.all()
    return render(req,"displayproduct.html",{'pdata':pdata})
def productedit(req,pid):
    cat = catdb.objects.all()
    pdata = productdb.objects.get(id=pid)
    return render(req,"editproduct.html",{'cat':cat,'pdata':pdata})
def updateproduct(req,pid):
    if req.method == "POST":
        se = req.POST.get('Select')
        na = req.POST.get('Name')
        de = req.POST.get('Des')
        pr = req.POST.get('Price')
        try:
            img = req.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=pid).pimage
        productdb.objects.filter(id=pid).update(pselect=se,pname=na,pdes=de,pprice=pr,pimage=file)
        return redirect(productdisplay)
def deleteproduct(req,pid):
    data = productdb.objects.get(id=pid)
    data.delete()
    return redirect(productdisplay)