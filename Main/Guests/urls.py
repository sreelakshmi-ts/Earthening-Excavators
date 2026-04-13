from django.urls import path
from Guests import views
app_name="webguest"
urlpatterns = [
    path('',views.Homepage,name="hopepage"),
    path('userreg/', views.userregistration,name="userreg"),
    path('ajaxplace/', views.Ajaxplace,name="Ajax-place"),
    path('shopreg/',views.shopregistration,name="shopreg"),
    path('login/',views.login,name="login"),
    
]