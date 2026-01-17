from django.contrib import admin
from django.urls import path
from auapp.views import uhome, usignup, uwelcome, ulogout, ucp,ulogin
from reppapp.views import home 
from fbapp.views import fb, about
from bdapp.views import prediction,result
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",uhome,name="uhome"),
    path("usignup",usignup,name="usignup"),
    path("uwelcome",uwelcome,name="uwelcome"),
    path("ulogout",ulogout,name="ulogout"),
    path("ucp",ucp,name="ucp"),
    path("home",home,name="home"),
    path("ulogin",ulogin,name="ulogin"),
    path("fb",fb,name="fb"),
    path("about",about,name="about"),
    path("predict",prediction,name="prediction"),
    path("result",result,name="result"),
]
