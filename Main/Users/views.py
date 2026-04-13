from django.shortcuts import render,redirect
from Guests.models import *
from Shops.models import *
from Admin.models import *
from Users.models import *
# Create your views here.
def userhome(request):
    if 'uid' in request.session:
        return render(request,"Users/UserHome.html")
    else:
        return redirect("weguest:login")
def userprofile(request):
    user=User.objects.get(id=request.session["uid"])
    return render(request,"Users/UserMyProfile.html",{'data':user})

def userediprofile(request):
    user=User.objects.get(id=request.session["uid"])
    if request.method=="POST":
        user.name=request.POST.get('txt_name')
        user.contact=request.POST.get('txt_contact')
        user.address=request.POST.get('txt_address')
        user.email=request.POST.get('txt_email')
        user.save()
        return redirect('webuser:userediprofile')
    else:
        return render(request,"Users/UserEditProfile.html",{'data':user})



def userchngpassword(request):
    user=User.objects.get(id=request.session["uid"])
    if request.method=="POST":
        pwd=user.password
        current=request.POST.get('txt_oldpass')
        if pwd == current:
            user=User.objects.get(id=request.session["uid"])
            new=request.POST.get('txt_newpass')
            user.password=new
            user.save()
            return redirect('webguest:login')
        else:
            error="Password Incorrect!!"
            return render(request,"Users/UserChangePassword.html",{'ER':error})
    else:
        return render(request,"Users/UserChangePassword.html")

def excsearch(request):
    cat=Category.objects.all()
    shoty=Shoptype.objects.all()
    subcat=Subcategory.objects.all()
    exc=Excavator.objects.all()
    return render(request,"Users/ExcavatorSearch.html",{'cat':cat,'shoty':shoty,'EXC':exc})
    



def get_excavator(request):
    if request.GET.get('tid')=="":
        if request.GET.get('sid')!="":
            subcat=Subcategory.objects.get(id=request.GET.get('sid'))
            exc=Excavator.objects.filter(subcategory=subcat)
            return render(request,"Users/GetExcavator.html",{'EXC':exc})
        else:
            cat=Subcategory.objects.get(id=request.GET.get('sid'))
            exc=Excavator.objects.filter(subcategory__category=cat)
            return render(request,"Users/GetExcavator.html",{'EXC':exc})
    else:
        tp=Shoptype.objects.get(id=request.GET.get('tid'))
        if request.GET.get('sid')!="":
            subcat=Subcategory.objects.get(id=request.GET.get('sid'))
            exc=Excavator.objects.filter(subcategory=subcat,shoptype=tp)
            return render(request,"Users/GetExcavator.html",{'EXC':exc})
        elif request.GET.get('cid')!="":
            cat=Subcategory.objects.get(id=request.GET.get('sid'))
            exc=Excavator.objects.filter(subcategory__category=cat,shoptype=tp)
            return render(request,"Users/GetExcavator.html",{'EXC':exc})
        else:
            exc=Excavator.objects.filter(shoptype=tp)
            return render(request,"Users/GetExcavator.html",{'EXC':exc})



def booknow(request,did):
    book=Booking.objects.all()
    data=Excavator.objects.get(id=did)
    user=User.objects.get(id=request.session["uid"])
    if request.method=="POST":
        exc=Excavator.objects.get(id=did)
        use=User.objects.get(id=request.session["uid"])
        Booking.objects.create(excavator=exc,user=use)
        return render(request,"Users/BookNow.html",{'Data':data})
    else:
        return render(request,"Users/BookNow.html",{'Data':data}) 


def Rent(request,eid):
    rent=Renting.objects.all()
    data=Excavator.objects.get(id=eid)
    shopid=data.shop_id
    request.session["shops"]=shopid
    user=User.objects.get(id=request.session["uid"])
    if request.method=="POST":
        exc=Excavator.objects.get(id=eid)
        use=User.objects.get(id=request.session["uid"])
        Renting.objects.create(quantity=request.POST.get("txt_quantity"),
                            from_date=request.POST.get("txt_fromdate"),days=request.POST.get("txt_date"),
                            amount=request.POST.get("txt_amount"),excavator=exc,user=use)
        return render(request,"Users/RentIt.html",{'Data':data})
    else:
        return render(request,"Users/RentIt.html",{'Data':data})


def mybook(request):
    book=Booking.objects.all()
    return render(request,"Users/MyBookings.html",{'book':book})



def cancelbook(request,eid):
    data=Booking.objects.get(id=eid)
    data.booking_vsts=3
    data.save()
    return redirect("webuser:mybookings")


def myrent(request):
    userdata=User.objects.get(id=request.session["uid"])
    rent=Renting.objects.filter(user=userdata)
    return render(request,"Users/MyRenting.html",{'rent':rent})


def cancelrent(request,eid):
    data=Renting.objects.get(id=eid)
    data.rent_vsts=3
    data.save()
    return redirect("webuser:myrenting")


def myoperatorreq(request):
    userdata=User.objects.get(id=request.session["uid"])
    data=AssignOperator.objects.filter(request__user=userdata)
    return render(request,"Users/MyOperatorRequest.html",{'data':data})

def CancelOprReq(request,eid):
    data=Renting.objects.get(id=eid)
    data.rent_vsts=3
    data.save()
    return redirect("webuser:myopreq")

def reqoperator(request):
    req=Requestoperator.objects.all()
    userid=User.objects.get(id=request.session["uid"])
    shp=Shop.objects.get(id=request.session["shops"])
    rent=Renting.objects.filter(user=userid).last()
    if request.method=="POST":
     
        Requestoperator.objects.create(request=request.POST.get("txt_request"),user=userid,shop=shp,rent=rent)
        return render(request,"Users/OperatorRequest.html",{'req':req})
    else:
        return render(request,"Users/OperatorRequest.html",{'req':req})



def excgallery(request,eid):
    exc=Excavator.objects.get(id=eid)
    gal=Gallery.objects.filter(excavator=exc)
    return render(request,"Users/ViewGallery.html",{'gal':gal})


def mycomplaint(request):
    comp= Complaint.objects.all()
    userid=User.objects.get(id=request.session["uid"])
    complaintyp=Complainttype.objects.all()
    if request.method=="POST":
        ctype=Complainttype.objects.get(id=request.POST.get('ddlcomplaint'))
        Complaint.objects.create(complaint_details=request.POST.get("txt_complaint"),user=userid,complainttype=ctype)
        return render(request,"Users/Complaint.html",{'comp':comp,'complaintyp':complaintyp})
    else:
        return render(request,"Users/Complaint.html",{'comp':comp,'complaintyp':complaintyp})


def myfeedback(request):
    
    userid=User.objects.get(id=request.session["uid"])
    feed=Feedback.objects.filter(user=userid)
    if request.method=="POST":

        Feedback.objects.create(feedback_details=request.POST.get("txt_feedback"),user=userid)
        return render(request,"Users/Feedback.html",{'feed':feed})
    else:
        return render(request,"Users/Feedback.html",{'feed':feed})




def BOOKPAYMENT(request,did):   
    if 'uid' in request.session:
        if request.method=="POST": 
            ids=Booking.objects.get(id=did)
            ids.booking_vsts=4
            ids.save()
            return redirect("webuser:processpayment")
        else:
            return render(request,"Users/BookingPayment.html")
    else:    
        return redirect("webguest:login")




def RENTPAYMENT(request,did):   
    if 'uid' in request.session:
        if request.method=="POST": 
            ids=Renting.objects.get(id=did)
            ids.rent_vsts=4
            ids.save()
            return redirect("webuser:processpayment")
        else:
            return render(request,"Users/RentPayment.html")
    else:    
        return redirect("webguest:login")



def Processingpayment(request):
    if 'uid' in request.session:
        return render(request,"Users/Runpayment.html")
    else:
        return redirect("webguest:login")
            


def Paysucess(request):
   if 'uid' in request.session:
        return render(request,"Users/Paysucessful.html")
   else:
       return redirect("webguest:login")





def Logout(request):
    del request.session["uid"]
    return redirect("webguest:hopepage")





