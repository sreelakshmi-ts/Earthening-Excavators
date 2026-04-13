
from django.urls import path
from Basics import views
urlpatterns = [
    path('calc/', views.calc,name="calc"),
    path('large/', views.large,name="large"),
    path('salary/',views.salary,name="salary"),
]
