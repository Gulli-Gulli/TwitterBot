"""appointment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="Welcome"),
    path('user/', views.userlogin, name="userlogin"),
    path('ureg/', views.uregistraction, name="UserReg"),
    path('uregaction/', views.uregaction, name="uregaction"),
    path('ulogin/', views.ulogin, name="ulogin"),
    path('uhome/', views.uhome, name="uhome"),
    path('ulogout/', views.ulogout, name="ulogout"),
    path('alogin/', views.adminlogindef, name="adminlogindef"),
    path('adminloginaction/', views.adminloginactiondef, name="adminloginactiondef"),
    path('uploaddataset/', views.uploaddataset, name="uploaddataset"),
    path('xlupload/', views.xlupload, name="xlupload"),    
    path('adminhome/', views.adminhomedef, name="adminhome"),
    path('adminlogout/', views.adminlogoutdef, name="adminlogout"),
    path('predictions/', views.predictions, name="predictions"),

    path('naivetest/', views.naivetest, name="naivetest"),
    path('nntest/', views.nntest, name="nntest"),
    path('svmtest/', views.svmtest, name="svmtest"),

    
    path('naiveprediction/', views.naiveprediction, name="naiveprediction"),
    path('nnprediction/', views.nnprediction, name="nnprediction"),
    path('svmprediction/', views.svmprediction, name="svmprediction"),

    path('graphview/', views.graphview, name="graphview"),
    path('viewpprofile/', views.viewpprofile, name="viewpprofile"),
    path('tweetssearch/', views.tweetssearch, name="tweetssearch"),
    path('viewmalw/', views.viewmalw, name="viewmalw"),

 




    

    
]
