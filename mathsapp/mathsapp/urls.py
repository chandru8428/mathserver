from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('mathserver/',views.findpower,name="mathserver"),
    path('',views.findpower,name="mathserverroot")
]