from django.shortcuts import render,redirect
from Guests.models import *
from Admin.models import *
from Shops.models import *
from Users.models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def shophome(request):
    if 'sid' in request.session:
        return render(request,"Shops/ShopHome.html")
    else:
        return redirect("webguest:login")

def shopprofile(request):
     shop=Shop.objects.get(id=request.session["sid"])
     return render(request,"Shops/ShopMyProfile.html", {'data':shop})

def shopediprofile(request):
    shop=Shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        shop.name=request.POST.get('txt_name')
        shop.contact=request.POST.get('txt_contact')
        shop.address=request.POST.get('txt_address')
        shop.email=request.POST.get('txt_email')
        shop.save()
        return redirect('webshop:shopediprofile')
    else:
        return render(request,"Shops/ShopEditProfile.html", {'data':shop})

def shopchngpassword(request):
    shop=Shop.objects.get(id=request.session["sid"])
    if request.method=="POST":
        pwd=shop.password
        current=request.POST.get('txt_oldpass')
        if pwd == current:
            shop=Shop.objects.get(id=request.session["sid"])
            new=request.POST.get('txt_newpass')
            shop.password=new
            shop.save()
            return redirect('webguest:login')
        else:
            error="Password Incorrect!!"
            return render(request,"Shops/ShopChangePassword.html",{'ER':error})
    else:
        return render(request,"Shops/ShopChangePassword.html")


def operatorregistration(request):
    dis=District.objects.all()
    shopid=Shop.objects.get(id=request.session["sid"])
    pla=Place.objects.all()
    opr=Operator.objects.all()
    if request.method=="POST":
         pl=Place.objects.get(id=request.POST.get('ddlplace'))
         Operator.objects.create(shop=shopid,name=request.POST.get("txt_name"),email=request.POST.get("txt_email"),password=request.POST.get("txt_password"),contact=request.POST.get("txt_contact"),address=request.POST.get("txt_address"),place=pl,photo=request.FILES.get("file_photo"),proof=request.FILES.get("file_proof"))
         return render(request,"Shops/OperatorsRegistration.html",{'operator':opr})
    else:
        return render(request,"Shops/OperatorsRegistration.html",{'dis':dis,'pl':pla,'operator':opr}) 


def DelOperator(request,did):
    opr=Operator.objects.get(id=did).delete()
    if request.method=="POST":
        opr.name.request.POST.get("txt_name"),opr.email.request.POST.get("txt_email"),opr.contact.request.POST.get("txt_contact"),opr.address.request.POST.get("txt_address"),opr.place==pl,opr.photo.request.POST.get("file_photo"),opr.proof.request.POST.get("file_proof")
        return redirect("webshop:operatorreg")
    else:
        return render(request,"Shops/OperatorsRegistration.html",{'dis':dis,'pl':pla ,'opr':opr}) 


def Excavatoradd(request):
    cat=Category.objects.all()
    shoty=Shoptype.objects.all()
    brandty=Brandtype.objects.all()
    shopid=Shop.objects.get(id=request.session["sid"])
    subcat=Subcategory.objects.all()
    exca=Excavator.objects.all()
    if request.method=="POST":
        sub=Subcategory.objects.get(id=request.POST.get('ddlsubcategory'))
        shopty=Shoptype.objects.get(id=request.POST.get('ddltype'))
        brandtype=Brandtype.objects.get(id=request.POST.get('ddlbrand'))
        Excavator.objects.create(shop=shopid,name=request.POST.get("txt_name"),subcategory=sub,details=request.POST.get("txt_details"),price=request.POST.get("txt_price"),brandtype=brandtype,shoptype=shopty,image=request.FILES.get("file_photo"))
        return render(request,"Shops/AddExcavators.html",{'excavator':exca})
    else:
        return render(request,"Shops/AddExcavators.html",{'cat':cat,'subcat':subcat,'excavator':exca,'shoty':shoty,'brandty':brandty})

    
def Delexcavator(request,did):
    Excavator.objects.get(id=did).delete()
    return redirect("webshop:excavatoradd")
    



def Ajaxplace(request):
    dis=District.objects.get(id=request.GET.get('disd'))
    pl=Place.objects.filter(district=dis)
    return render(request,"Guests/Ajaxplace.html",{'data':pl})

def Ajaxsubcategory(request):
    cate=Category.objects.get(id=request.GET.get('categ'))
    subcate=Subcategory.objects.filter(category=cate)
    return render(request,"Shops/AjaxSubcategory.html",{'data':subcate})




def viewbooking(request):
    book=Booking.objects.filter(booking_vsts=0)
    return render(request,"Shops/ViewBookings.html",{'book':book})

def acceptbooking(request,aid):
    book=Booking.objects.get(id=aid)
    book.booking_vsts=1
    name=book.user.name
    email=book.user.email
    book.save()
    send_mail('Respected Sir/Madam '+name,#subject
    "Your Booking is successfull, Thank you for choosing us",#body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return redirect("webshop:viewbook")


def rejectbooking(request,rid):
    book=Booking.objects.get(id=rid)
    book.booking_vsts=2
    name=book.user.name
    email=book.user.email
    book.save()
    send_mail('Respected Sir/Madam '+name,#subject
    "Sorry your booking is canceled",#body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return redirect("webshop:viewbook")

def acceptedbooklist(request):
    book=Booking.objects.filter(booking_vsts=1)
    return render(request,"Shops/AcceptedBooking.html",{'book':book})


def rejectedbooklist(request):
    book=Booking.objects.filter(booking_vsts=2)
    return render(request,"Shops/RejectedBooking.html",{'book':book})

def bookpayedlist(request):
    book=Booking.objects.filter(booking_vsts=4)
    return render(request,"Shops/BookingPayedList.html",{'book':book})

def Cancelbooklist(request):
    book=Booking.objects.filter(booking_vsts=3)
    return render(request,"Shops/CanceldBookingList.html",{'book':book})


def viewrenting(request):
    rent=Renting.objects.filter(rent_vsts=0)
    return render(request,"Shops/ViewRenting.html",{'rent':rent})


def accepterenting(request,aid):
    rent=Renting.objects.get(id=aid)
    rent.rent_vsts=1
    name=rent.user.name
    email=rent.user.email
    rent.save()
    send_mail('Respected Sir/Madam '+name,#subject
    "Your Renting is successfull, Thank you for choosing us",#body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return redirect("webshop:viewrent")

def rejectrenting(request,rid):
    rent=Renting.objects.get(id=rid)
    rent.rent_vsts=2
    name=rent.user.name
    email=rent.user.email
    rent.save()
    send_mail('Respected Sir/Madam '+name,#subject
    "Your Renting is Canceled",#body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return redirect("webshop:viewrent")


def acceptedrentlist(request):
    rent=Renting.objects.filter(rent_vsts=1)
    return render(request,"Shops/AcceptedRenting.html",{'rent':rent})

def rejectedrentlist(request):
    rent=Renting.objects.filter(rent_vsts=2)
    return render(request,"Shops/RejectedRenting.html",{'rent':rent})


def rentpayedlist(request):
    rent=Renting.objects.filter(rent_vsts=4)
    return render(request,"Shops/RentPayedList.html",{'rent':rent})


def Cancelrentlist(request):
    rent=Renting.objects.filter(rent_vsts=3)
    return render(request,"Shops/CanceledRenting.html",{'rent':rent})



def viewReq(request):
    req=Requestoperator.objects.filter(request_vsts=0)
    return render(request,"Shops/ViewOperatorRequest.html",{'req':req})


def requestaccept(request,aid):
    req=Requestoperator.objects.get(id=aid)
    req.request_vsts=1
    req.save()
    return redirect("webshop:viewreq")


def requestreject(request,rid):
    req=Requestoperator.objects.get(id=rid)
    req.request_vsts=2
    req.save()
    return redirect("webshop:viewreq")

def acceptedrequestlist(request):
    req=Requestoperator.objects.filter(request_vsts=1)
    return render(request,"Shops/AcceptedRequest.html",{'req':req})


def rejectedrequestlist(request):
    req=Requestoperator.objects.filter(request_vsts=2)
    return render(request,"Shops/RejectedRequest.html",{'req':req})

def CancelReqlist(request):
    req=Requestoperator.objects.filter(request_vsts=3)
    return render(request,"Shops/CanceledOperReq.html",{'req':req})

def viewopr(request,reqid):
    shopid=Shop.objects.get(id=request.session["sid"])
    opr=Operator.objects.filter(shop=shopid)
    request.session["req"]=reqid
    return render(request,"Shops/ViewOperators.html",{'opr':opr})


def workassign(request,oprid):
    opr=Operator.objects.get(id=oprid)
    req=Requestoperator.objects.get(id=request.session["req"])
    AssignOperator.objects.create(operator=opr, request=req)
    return redirect("webshop:shophome")




def gallery(request,eid):
    exca=Excavator.objects.get(id=eid)
    gal=Gallery.objects.all()
    if request.method=="POST":
        Gallery.objects.create(image=request.FILES.get("file_photo"),excavator=exca)
        return render(request,"Shops/Gallery.html",{'gal':gal})
    else:
        return render(request,"Shops/Gallery.html",{'gal':gal})


def Delimage(request,did):
    Gallery.objects.get(id=did).delete()
    return redirect("webshop:gallery")

def mycomplaint(request):
    shopid=Shop.objects.get(id=request.session["sid"])
    comp= Complaint.objects.filter(shop=shopid)
    complaintyp=Complainttype.objects.all()
    if request.method=="POST":
        ctype=Complainttype.objects.get(id=request.POST.get('ddlcomplaint'))
        Complaint.objects.create(complaint_details=request.POST.get("txt_complaint"),shop=shopid,complainttype=ctype)
        return render(request,"Shops/Complaint.html",{'comp':comp,'complaintyp':complaintyp})
    else:
        return render(request,"Shops/Complaint.html",{'comp':comp,'complaintyp':complaintyp})



def myfeedback(request):
    
    shopid=Shop.objects.get(id=request.session["sid"])
    feed=Feedback.objects.filter(shop=shopid)
    if request.method=="POST":

        Feedback.objects.create(feedback_details=request.POST.get("txt_feedback"),shop=shopid)
        return render(request,"Shops/Feedback.html",{'feed':feed})
    else:
        return render(request,"Shops/Feedback.html",{'feed':feed})



def Logout(request):
    del request.session["sid"]
    return redirect("webguest:hopepage")






