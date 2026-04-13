from django.shortcuts import render

# Create your views here.
def calc(request):
    if request.method=="POST":
        num1=int(request.POST.get('txt_num1'))
        num2=int(request.POST.get('txt_num2'))
        btn=request.POST.get('btn')
        if btn=="+":
            result=num1+num2
        if btn=="-":
            result=num1-num2
        if btn=="*":
            result=num1*num2
        if btn=="/":
            result=num1/num2
        return render(request,"Basics/Calculator.html",{'res':result})
    else:
        return render(request,"Basics/Calculator.html")
def large(request):
    if request.method=="POST":
        num1=int(request.POST.get('txt_num1'))
        num2=int(request.POST.get('txt_num2'))
        btn=request.POST.get('btn_result')
        if num1>num2:
            largest=num1
        else:
            largest=num2
        if num1<num2:
            samllest=num1
        else:
            smallest=num2
        return render(request,"Basics/largest.html",{'lag':largest,'smal':smallest})
        
    else:
        return render(request,"Basics/largest.html")
def salary(request):
    if request.method=="POST":
        firstname=(request.POST.get('txt_frstname'))
        lastname=(request.POST.get('txt_lastname'))
        gen=(request.POST.get('gender'))
        martl=(request.POST.get('martial'))
        dept=(request.POST.get('ddldepartment'))
        bs=int(request.POST.get('txt_salary'))
        if bs>=1000:
            ta=bs*.4
            da=bs*.35
            hra=bs*.3
            lic=bs*.25
            pf=bs*.2 
            deduction=lic+pf
            netamount=bs+ta+da+hra-(lic+pf)   
        elif bs>=5000 and bs<1000:
            ta=bs*.35
            da=bs*.3
            hra=bs*.25
            lic=bs*.2
            pf=bs*.15
            deduction=lic+pf
            netamount=bs+ta+da+hra-(lic+pf)
        elif bs<5000:
            ta=bs*.3
            da=bs*.25
            hra=bs*.2
            lic=bs*.15
            pf=bs*.1
            deduction=lic+pf
            netamount=bs+ta+da+hra-(lic+pf)
        name=firstname+lastname
        return render(request,"Basics/Salarycalc.html",{'fstna':name,'ge':gen,'mar':martl,'dep':dept,'bcs':bs,'ta':ta,'da':da,'hra':hra,'lic':lic,'pf':pf,'ded':deduction,'net':netamount})
    else:
        return render(request,"Basics/Salarycalc.html") 