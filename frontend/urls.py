from django.urls import path
from frontend import views

urlpatterns = [
    path('websitepage/',views.websitepage,name="websitepage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('carpage/<cat_name>',views.carpage,name="carpage"),
    path('detailpage/<int:pid>/',views.detailpage,name="detailpage"),
    path('regpage/',views.regpage,name="regpage"),
    path('signpage/',views.signpage,name="signpage"),
    path('savereg/',views.savereg,name="savereg"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('savecart/',views.savecart,name="savecart"),
    path('delitem/<int:cartid>/',views.delitem,name="delitem"),
    path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
    path('savebill/',views.savebill,name="savebill")

]