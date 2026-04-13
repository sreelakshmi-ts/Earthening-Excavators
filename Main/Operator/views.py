from django.shortcuts import render,redirect
from Shops.models import *
from  .models import *
from Guests.models import *
from Users.models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def operatorhome(request):
    if 'oid' in request.session:
        return render(request,"Operator/OperatorHomePage.html")
    else:
        return redirect("webguest:login")

def operatorprofile(request):
    opr=Operator.objects.get(id=request.session["oid"])
    return render(request,"Operator/OperatorMyProfile.html", {'data':opr})

def operatorediprofile(request):
    opr=Operator.objects.get(id=request.session["oid"])
    if request.method=="POST":
        opr.name=request.POST.get('txt_name')
        opr.contact=request.POST.get('txt_contact')
        opr.address=request.POST.get('txt_address')
        opr.email=request.POST.get('txt_email')
        opr.save()
        return redirect('weboperator:operediprofile')
    else:
        return render(request,"Operator/OperatorEditProfile.html", {'data':opr})


def operatorchngpassword(request):
    opr=Operator.objects.get(id=request.session["oid"])
    if request.method=="POST":
        pwd=opr.password
        current=request.POST.get('txt_oldpass')
        if pwd == current:
            opr=Operator.objects.get(id=request.session["oid"])
            new=request.POST.get('txt_newpass')
            opr.password=new
            opr.save()
            return redirect('webguest:login')
        else:
            error="Password Incorrect!!"
            return render(request,"Operator/OperatorChangePassword.html",{'ER':error})
    else:
        return render(request,"Operator/OperatorChangePassword.html")



def viewassigment(request):
    opr=Operator.objects.get(id=request.session["oid"])
    data=AssignOperator.objects.filter(operator=opr,assign_vsts=0)
    return render(request,"Operator/ViewAssignments.html",{'data':data})

def acceptassigment(request,aid):
    data=AssignOperator.objects.get(id=aid)
    data.assign_vsts=1
    name=data.request.user.name
    email=data.request.user.email
    data.save()
    send_mail('Respected Sir/Madam '+name,#subject
    "Your Operator Request is accepted Successfully",#body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return redirect("weboperator:assigments")

def rejectassigment(request,rid):
    data=AssignOperator.objects.get(id=rid)
    data.assign_vsts=2
    name=data.request.user.name
    email=data.request.user.email
    data.save()
    send_mail('Respected Sir/Madam '+name,#subject
    "Your Operator Request is accepted Successfully",#body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return redirect("weboperator:assigments")

def acceptedassignmentlist(request):
    data=AssignOperator.objects.filter(assign_vsts=1)
    return render(request,"Operator/AcceptedAssignment.html",{'data':data})

def rejectassigmentlist(request):
    data=AssignOperator.objects.filter(assign_vsts=2)
    return render(request,"Operator/RejectedAssignment.html",{'data':data})



def Logout(request):
    del request.session["oid"]
    return redirect("webguest:hopepage")






