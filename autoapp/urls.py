from django.urls import path
from autoapp import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('loginadmin/',views.loginadmin,name="loginadmin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('catpage/',views.catpage,name="catpage"),
    path('savecata/',views.savecata,name="savecata"),
    path('catdisplay/',views.catdisplay,name="catdisplay"),
    path('catedit/<int:catid>/',views.catedit,name="catedit"),
    path('updatecat/<int:catid>/',views.updatecat,name="updatecat"),
    path('deletecat/<int:catid>/',views.deletecat,name="deletecat"),
    path('productpage/',views.productpage,name="productpage"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('productdisplay/',views.productdisplay,name="productdisplay"),
    path('productedit/<int:pid>/',views.productedit,name="productedit"),
    path('updateproduct/<int:pid>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:pid>/',views.deleteproduct,name="deleteproduct")

]