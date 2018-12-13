"""Bigfitproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Bigfit import views
from django.conf.urls import url

urlpatterns = [
    # path('admin/', admin.site.urls),
    #path('login/', views.login, name='login page'),
    path('index/', views.index, name='index page'),
    #path('register/', views.register, name='register page'),
    #path('logout/', views.logout),
    path('weightinput/', views.weightinput),
    path('calorieinput/', views.calorieinput),
    path('weighthistory/', views.weighthistory),
    path('caloriehistory/', views.caloriehistory),
    path('viewprofile/', views.viewprofile),
    path('deleteweight/', views.deleteweighthistory),
    path('deletecalorie/', views.deletecaloriehistory),
    path('editcalorie/', views.editcaloriehistory),
    path('editweight/', views.editweighthistory),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^about/', views.about, name='about'),
    url(r'^logout/', views.logout, name='logout'),
    path('editusername/', views.editusername, name='editusername'),
    path('editgender/', views.editgender, name='editgender'),
    path('edittargetweight/', views.edittargetweight),
    path('editfeet/', views.editfeet),
    path('editinches/', views.editinches),
    path('editzipcode/', views.editzipcode),
    path('editdob/', views.editdob),
    path('editpassword/', views.editpassword, name='editpassword')


]
