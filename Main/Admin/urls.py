from django.urls import path
from Admin import views

app_name="webadmin"
urlpatterns = [
    path('adminhome/', views.Adminhome,name="adminhome"),
    path('dis/', views.district,name="dis"),
    path('cat/', views.category,name="cat"),
    path('deldis/<int:did>', views.Deldistrict,name="deldistrict"),
    path('delcat/<int:did>', views.Delcategory,name="delcategory"),
    path('edidis/<int:eid>', views.Edidistrict,name="edidistrict"),
    path('edicat/<int:eid>', views.Editcategory,name="edicategory"),
    path('pla/', views.place,name="pla"),
    path('delpla/<int:did>', views.Delplace,name="delplace"),
    path('edipla/<int:eid>', views.Ediplace,name="ediplace"), 

    path('subcat/',views.subcategory,name="subcat"),
    path('delsubcat/<int:did>', views.Delsubcategory,name="delsubcategory"),
    path('edisubcat/<int:eid>', views.Edisubcategory,name="edisubcategory"), 

    path('shoptype/',views.shoptype,name="shoptype"),
    path('delshoptype/<int:did>' ,views.Delshoptype,name="delshoptype"),

    path('complainttype/',views.Complaintype,name="complainttype"),
    path('delcomplaintype/<int:did>',views.Delcomplainttype,name="delcomplaintype"),

    path('brand/',views.Brand,name="brand"),
    path('delbrand/<int:did>',views.Brand,name="delbrand"),

    path('verify/',views.shopverify,name="verify"),
    path('acceptsh/<int:aid>',views.acceptshop,name="acceptsh"),
    path('rejectsh/<int:rid>',views.rejectshop,name="rejectsh"),

    path('accepted/',views.acceptlist,name="accepted"),
    path('rejected/',views.rejectlist,name="rejected"),

    path('compview/',views.viewcomplaint,name="compview"),

    path('reply/<int:reqid>',views.complaintreplay,name="reply"),

    path('feedbackview/',views.viewFeedback,name="feedbackview"),

    path('logout/',views.Logout,name="logout"),

]