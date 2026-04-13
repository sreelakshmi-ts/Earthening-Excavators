from django.shortcuts import render,redirect
from Admin.models import *
from .models import *
from Shops.models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def Homepage(request):
    return render(request,"Guests/HomePage.html")

def userregistration(request):
    dis=District.objects.all()
    pla=Place.objects.all()
    if request.method=="POST":
        pl=Place.objects.get(id=request.POST.get('ddlplace'))
        User.objects.create(name=request.POST.get("txt_name"),email=request.POST.get("txt_email"),contact=request.POST.get("txt_contact"),address=request.POST.get("txt_address"),place=pl,photo=request.FILES.get("file_photo"),proof=request.FILES.get("file_proof"),password=request.POST.get("txt_password"))
        send_mail('Respected Sir/Madam '+request.POST.get("txt_name"),#subject
        "Your account creat Successfully ",#body
        settings.EMAIL_HOST_USER,
        [request.POST.get("txt_email")],
        )
        return render(request,"Guests/UserRegistration.html")
    else:
        return render(request,"Guests/UserRegistration.html",{'dis':dis,'pl':pla})
    
      
def Ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disd'))
    pl=Place.objects.filter(district=dis)
    return render(request,"Guests/Ajaxplace.html",{'data':pl})

def shopregistration(request):
    dis=District.objects.all()
    pla=Place.objects.all()
    if request.method=="POST":
        pl=Place.objects.get(id=request.POST.get('ddlplace'))
        Shop.objects.create(name=request.POST.get("txt_name"),email=request.POST.get("txt_email"),contact=request.POST.get("txt_contact"),address=request.POST.get("txt_address"),place=pl,photo=request.FILES.get("file_photo"),proof=request.FILES.get("file_proof"),password=request.POST.get("txt_password"))
        return render(request,"Guests/Shopregistration.html")
    else:
        return render(request,"Guests/Shopregistration.html",{'dis':dis,'pl':pla})
    
def login(request):
    if request.method=="POST":
        admincount=Admin.objects.filter(email=request.POST.get('txt_email'),password=request.POST.get('txt_password')).count()
        usercount=User.objects.filter(email=request.POST.get('txt_email'),password=request.POST.get('txt_password')).count()
        shopcount=Shop.objects.filter(email=request.POST.get('txt_email'),password=request.POST.get('txt_password')).count()
        operatorcount=Operator.objects.filter(email=request.POST.get('txt_email'),password=request.POST.get('txt_password')).count()
        if admincount>0:
            admin=Admin.objects.get(email=request.POST.get('txt_email'),password=request.POST.get('txt_password'))
            request.session["aid"]=admin.id
            request.session["aname"]=admin.name
            return redirect("webadmin:adminhome")
        if usercount>0:
            user=User.objects.get(email=request.POST.get('txt_email'),password=request.POST.get('txt_password'))
            request.session["uid"]=user.id
            request.session["uname"]=user.name
            return redirect("webuser:userhome")
        elif shopcount>0:
            shop=Shop.objects.get(email=request.POST.get('txt_email'),password=request.POST.get('txt_password'))
            request.session["sid"]=shop.id
            request.session["sname"]=shop.name
            return redirect("webshop:shophome")
        
        elif operatorcount>0:
            opr=Operator.objects.get(email=request.POST.get('txt_email'),password=request.POST.get('txt_password'))
            request.session["oid"]=opr.id
            request.session["oname"]=opr.name
            return redirect("weboperator:operatorhome")
        

    return render(request,"Guests/Login.html")
