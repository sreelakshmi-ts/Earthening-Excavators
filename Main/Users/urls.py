from django.urls import path
from Users import views
app_name="webuser"
urlpatterns = [
    path('userhome/', views.userhome,name="userhome"),
    path('userprofile/',views.userprofile,name="userprofile"),
    path('userediprofile/',views.userediprofile,name="userediprofile"),
    path('userchngpassword/',views.userchngpassword,name="userchngpassword"),

    path('srchexcavator/',views.excsearch,name="srchexcavator"),   
    path('getexcavator/',views.get_excavator,name="Get_Excavator"),

    path('bookit/<int:did>',views.booknow,name="bookit"),

    path('rentit/<int:eid>',views.Rent,name="rentit"),

    path('mybookings/',views.mybook,name="mybookings"),

    path('myrenting/',views.myrent,name="myrenting"),

    path('operatorreq/',views.reqoperator,name="operatorreq"),

    path('myopreq/',views.myoperatorreq,name="myopreq"),

    path('viewgallery/<int:eid>',views.excgallery,name="viewgallery"),

    path('usercomplaint/',views.mycomplaint,name="usercomplaint"),

    path('userfeedback/',views.myfeedback,name="userfeedback"),

    path('cancelbooking/<int:eid>',views.cancelbook,name="cancelbooking"),

    path('cancelrenting/<int:eid>',views.cancelrent,name="cancelrenting"),

    path('cancelrequest/<int:eid>',views.CancelOprReq,name="cancelrequest"),

    path('bookpayment/<int:did>',views.BOOKPAYMENT,name="bookpayment"),

    path('rentpayment/<int:did>', views.RENTPAYMENT,name="rentpayment"),

    path('processpayment/',views.Processingpayment,name="processpayment"),

    path('paysuccess/',views.Paysucess,name="paysuccess"),

    path('logout/',views.Logout,name="logout"),
    
]