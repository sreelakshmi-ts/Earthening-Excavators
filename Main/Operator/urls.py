from django.urls import path
from Operator import views
app_name="weboperator"
urlpatterns = [
    path('operatorhome/',views.operatorhome,name="operatorhome"),

    path('operprofile/',views.operatorprofile,name="operprofile"),

    path('operediprofile/',views.operatorediprofile,name="operediprofile"),

    path('operatorchngpass/',views.operatorchngpassword,name="operatorchngpass"),

    path('assigments/',views.viewassigment,name="assigments"),

    path('acceptassign/<int:aid>',views.acceptassigment,name="acceptassign"),

    path('rejectassign/<int:rid>',views.rejectassigment,name="rejectassign"),

    path('acceptedassignlist/',views.acceptedassignmentlist,name="acceptedassignlist"),

    path('rejectedassignlist/',views.rejectassigmentlist,name="rejectedassignlist"),

    path('logout/',views.Logout,name="logout"),
]