from django.urls import path
from Shops import views
app_name="webshop"
urlpatterns = [
    path('shophome/', views.shophome,name="shophome"),

    path('shopprofile/', views.shopprofile, name="shopprofile"),

    path('shopediprofile/',views.shopediprofile, name="shopediprofile"),

    path('shopchngpassword/',views.shopchngpassword, name="shopchngpassword"),

    path('operatorreg/',views.operatorregistration,name="operatorreg"),

    path('deloperator/<int:did>', views.DelOperator,name="deloperator"),

    path('excavatoradd/',views.Excavatoradd, name="excavatoradd"),

    path('delexcavator/<int:did>',views.Delexcavator,name="delexcavator"),

    path('ajaxsubcategory/',views.Ajaxsubcategory, name="Ajax-subcategory"),

    path('viewbook/',views.viewbooking,name="viewbook"),

    path('acceptbook/<int:aid>',views.acceptbooking,name="acceptbook"),

    path('rejectbook/<int:rid>',views.rejectbooking,name="rejectbook"),

    path('acceptedlist/',views.acceptedbooklist,name="acceptedlist"),

    path('rejectedlist/',views.rejectedbooklist,name="rejectedlist"),

    path('viewrent/',views.viewrenting,name="viewrent"),

    path('accepterent/<int:aid>',views.accepterenting,name="accepterent"),

    path('rejectrent/<int:rid>',views.rejectrenting,name="rejectrent"),

    path('acceptedrentings/',views.acceptedrentlist,name="acceptedrentings"),

    path('rejectedrentings/',views.rejectedrentlist,name="rejectedrentings"),

    path('viewreq/',views.viewReq,name="viewreq"),

    path('acceptrequest/<int:aid>',views.requestaccept,name="acceptrequest"),

    path('rejectrequest/<int:rid>',views.requestreject,name="rejectrequest"),

    path('acceptedreqs/',views.acceptedrequestlist,name="acceptedreqs"),

    path('rejectedreqs/',views.rejectedrequestlist,name="rejectedreqs"),

    path('viewoperator/<int:reqid>',views.viewopr,name="viewoperator"),

    path('assignopr/<int:oprid>',views.workassign,name="assignopr"),

    path('gallery/<int:eid>',views.gallery,name="gallery"),

    path('delimg/<int:did>',views.Delimage,name="delimg"),


    path('shopcomplaint/',views.mycomplaint,name="shopcomplaint"),

    path('shopfeedback/',views.myfeedback,name="shopfeedback"),

    path('canceledbook/',views.Cancelbooklist,name="canceledbook"),

    path('canceledrent/',views.Cancelrentlist,name="canceledrent"),

    path('canceledrequest/',views.CancelReqlist,name="canceledrequest"),

    path('payedbook/',views.bookpayedlist,name="payedbook"),

    path('payedrent/',views.rentpayedlist,name="payedrent"),
    
    path('logout/',views.Logout,name="logout"),



]