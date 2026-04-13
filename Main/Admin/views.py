from django.shortcuts import render,redirect
from .models import *
from Guests.models import *
from Shops.models import Operator
from Users.models import Booking
# Create your views here.
def Adminhome(request):
    if 'aid' in request.session:
        shopcount=Shop.objects.all().count()
        usercount=User.objects.all().count()
        operatorcount=Operator.objects.all().count()
        bookingcount=Booking.objects.all().count()
        data=Shop.objects.filter(shop_vsts=1)
        return render(request,"Admin/AdminHome.html",{'shopcount':shopcount,'usercount':usercount,'operatorcount':operatorcount,'bookingcount':bookingcount,'data':data})
    else:
        return redirect("webguest:login")


def district(request):
    dis=District.objects.all()
    if request.method=="POST":
        district=request.POST.get('txt_district')
        District.objects.create(name=district)
        return render(request,"Admin/District.html",{'dis':dis})
    else:
        return render(request,"Admin/District.html",{'dis':dis})
def category(request):
    cat=Category.objects.all()
    if request.method=="POST":
        category=request.POST.get('txt_category')
        Category.objects.create(name=category)
        return render(request,"Admin/Category.html",{'cat':cat})
    else:
        return render(request,"Admin/Category.html" ,{'cat':cat})

def Deldistrict(request,did):
    dis=District.objects.get(id=did).delete()
    return redirect("webadmin:dis")

def Delcategory(request,did):
    cat=Category.objects.get(id=did).delete()
    return redirect("webadmin:cat")


def Edidistrict(request,eid):
    dis=District.objects.all()
    dist=District.objects.get(id=eid)
    if request.method=="POST":
        dist.name=request.POST.get('txt_district')
        dist.save()
        return redirect("webadmin:dis")
    else:
        return render(request,"Admin/District.html",{'res':dist,'dis':dis})



def Editcategory(request,eid):
    cat=Category.objects.all()
    cate=Category.objects.get(id=eid)
    if request.method=="POST":
        cate.name=request.POST.get('txt_category')
        cate.save()
        return redirect("webadmin:cat")
    else:
        return render(request,"Admin/Category.html",{'res':cate,'cat':cat})


def place(request):
    dis=District.objects.all()
    pla=Place.objects.all()
    if request.method=="POST":
        dist=District.objects.get(id=request.POST.get('ddldistrict'))
        Place.objects.create(name=request.POST.get("txt_place"),district=dist)
        return render(request,"Admin/Place.html",{'dis':dis,'pla':pla})
    else:
        return render(request,"Admin/Place.html",{'dis':dis,'pla':pla})
def Delplace(request):
    pla=Place.objects.get(id=did).delete()
    return redirect("webadmin:pla")

def Ediplace(request,eid):
    pla=Place.objects.all()
    plac=Place.objects.get(id=eid)
    if request.method=="POST":
        plac.name=request.POST.get('txt_place')
        plac.save()
        return redirect("webadmin:pla")
    else:
        return render(request,"Admin/Place.html",{'res':plac,'pla':pla})    







def subcategory(request):
    cat=Category.objects.all()
    subcat=Subcategory.objects.all()
    if request.method=="POST":
        cate=Category.objects.get(id=request.POST.get('ddlcategory'))
        Subcategory.objects.create(name=request.POST.get("txt_subcategory"),category=cate)
        return render(request,"Admin/Subcategory.html",{'cat':cat,'subcat':subcat})
    else:
        return render(request,"Admin/Subcategory.html",{'cat':cat,'subcat':subcat})

def Delsubcategory(request):
    subcat=Subcategory.objects.get(id=did).delete()
    return redirect("webadmin:subcat")

def Edisubcategory(request,eid):
    subcat=Subcategory.objects.all()
    subcate=Subcategory.objects.get(id=eid)
    if request.method=="POST":
        subcate.name=request.POST.get('txt_subcategory')
        subcate.save()
        return redirect("webadmin:subcat")
    else:
        return render(request,"Admin/Subcategory.html",{'res':subcate,'subcat':subcat})




def shoptype(request):
    shoty=Shoptype.objects.all()
    if request.method=="POST":
        Shoptype.objects.create(shoptype=request.POST.get('txt_shoptype'))
        return render(request,"Admin/ShopType.html",{'shoty':shoty})
    else:
        return render(request,"Admin/ShopType.html",{'shoty':shoty})
def Delshoptype(request,did):
    shoty=Shoptype.objects.get(id=did).delete()
    return redirect("webadmin:shoptype")




def Complaintype(request):
    complainty=Complainttype.objects.all()
    if request.method=="POST":
        Complainttype.objects.create(complaintyp=request.POST.get('txt_complainttype'))
        return render(request,"Admin/ComplaintType.html",{'complainty':complainty})
    else:
        return render(request,"Admin/ComplaintType.html",{'complainty':complainty})

def Delcomplainttype(request,did):
    complainty=Complainttype.objects.get(id=did).delete()
    return redirect("webadmin:complainttype")




def Brand(request):
    brandty=Brandtype.objects.all()
    if request.method=="POST":
        Brandtype.objects.create(brandtype=request.POST.get('txt_brand'))
        return render(request,"Admin/Brand.html",{'brandty':brandty})
    else:
        return render(request,"Admin/Brand.html",{'brandty':brandty})

def Delbrand(request,did):
    brandty=Brandtype.objects.get(id=did).delete()
    return redirect("webadmin:brand")


def shopverify(request):
    shp=Shop.objects.filter(shop_vsts=0)
    return render(request,"Admin/ShopVerification.html",{'shp':shp})    

def acceptshop(request,aid):
    shp=Shop.objects.get(id=aid)
    shp.shop_vsts=1
    shp.save()
    return redirect("webadmin:verify")

def rejectshop(request,rid):
    shp=Shop.objects.get(id=rid)
    shp.shop_vsts=2
    shp.save()
    return redirect("webadmin:verify")


def acceptlist(request):
    shp=Shop.objects.filter(shop_vsts=1)
    return render(request,"Admin/AcceptedList.html",{'shp':shp})

def rejectlist(request):
    shp=Shop.objects.filter(shop_vsts=2)
    return render(request,"Admin/RejectedList.html",{'shp':shp})

def viewcomplaint(request):
    userdata=User.objects.all()
    shopdata=Shop.objects.all()
    datau=Complaint.objects.filter(user__in=userdata)
    datas=Complaint.objects.filter(shop__in=shopdata)
    return render(request,"Admin/ViewComplaint.html",{'datau':datau,'datas':datas})

def viewFeedback(request):
    userdata=User.objects.all()
    shopdata=Shop.objects.all()
    datau=Feedback.objects.filter(user__in=userdata)
    datas=Feedback.objects.filter(shop__in=shopdata)
    return render(request,"Admin/ViewFeedback.html",{'datau':datau,'datas':datas})

def complaintreplay(request,reqid):
    comp=Complaint.objects.get(id=reqid)
    if request.method=="POST":
        comp.complaint_replay=request.POST.get("txtreplay")
        comp.complaint_vsts=1
        comp.save()
        return redirect("webadmin:compview")
    else:
        return render(request,"Admin/Reply.html")



def Logout(request):
    del request.session["aid"]
    return redirect("webguest:hopepage")







