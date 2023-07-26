from django.shortcuts import render,redirect
from autoapp.models import catdb,productdb
from frontend.models import regdb,cartbd,billdb
from django.contrib import messages
# Create your views here.
def websitepage(req):
    cat= catdb.objects.all()
    return render(req,"website.html",{'cat':cat})
def aboutpage(req):
    cat = catdb.objects.all()
    return render(req,"aboutus.html",{'cat':cat})
def contactpage(req):
    cat = catdb.objects.all()
    return render(req,"contactus.html",{'cat':cat})
def carpage(req,cat_name):
    cat = catdb.objects.all()
    pro = productdb.objects.filter(pselect=cat_name)
    return render(req,"cars.html",{'cat':cat,'pro':pro})
def detailpage(req,pid):
    cat = catdb.objects.all()
    pdata = productdb.objects.get(id=pid)
    return render(req,"cardetails.html",{'cat':cat,'pdata':pdata})
def regpage(req):
    return render(req,"registration.html")
def signpage(req):
    return render(req,"signin.html")
def savereg(request):
    if request.method =="POST":
        rn = request.POST.get('Username')
        re = request.POST.get('Email')
        rm = request.POST.get('Mobile')
        rp = request.POST.get('Password')
        rimg = request.FILES['Image']
        obj = regdb(rname=rn,remail=re,rmobile=rm,rpas=rp,rimage=rimg)
        obj.save()
        return redirect(regpage)
def userlogin(request):
    if request.method =="POST":
        uname = request.POST.get('Username')
        pwd = request.POST.get('Password')
        if regdb.objects.filter(rname=uname,rpas=pwd).exists():
            request.session['Username']=uname
            request.session['Password']=pwd
            messages.success(request, "Sign in Successfull ")
            return redirect(websitepage)
        else:
            messages.error(request, "Failed ")
            return redirect(signpage)
        messages.error(request, "Failed ")
    return redirect(signpage)
def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logout successful ")
    return redirect(signpage)
def cartpage(request):
    cat = catdb.objects.all()
    cdata = cartbd.objects.filter(uname=request.session['Username'])
    total_price = 0
    for i in cdata:
        total_price = total_price + i.ptotal
    return render(request,'cartpage.html',{'cat':cat,'cdata':cdata,'total_price':total_price})
def savecart(request):
    if request.method=="POST":
        un = request.POST.get('Uname')
        pn = request.POST.get('Name')
        pd = request.POST.get('Description')
        pq = request.POST.get('Qty')
        pp = request.POST.get('Price')
        pt = request.POST.get('Total')
        obj = cartbd(uname=un,pname=pn,pdes=pd,pqu=pq,pprice=pp,ptotal=pt)
        obj.save()
        messages.success(request, "Item added to cart ")
        return redirect(websitepage)
def delitem(request,cartid):
    cdata = cartbd.objects.filter(id=cartid)
    cdata.delete()
    messages.success(request, "Item Deleted ")
    return redirect(cartpage)
def checkoutpage(request):
    cdata = cartbd.objects.filter(uname=request.session['Username'])
    total_price =0
    for i in cdata:
        total_price = total_price+i.ptotal
    return render(request,"checkout.html" ,{'cdata':cdata,'total_price':total_price})
def savebill (request):
    if request.method=="POST":
        na = request.POST.get('User')
        em = request.POST.get('Email')
        ad = request.POST.get('Address')
        mo = request.POST.get('Mobile')
        obj= billdb(name=na,email=em,address=ad,mobile=mo)
        obj.save()
        messages.success(request, "Order placed successfully ")
        return redirect(websitepage)