"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from MyApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/',views.sample,name='sample'),
    path('home/',views.home,name='home'),
    path('hello/<str:name>/',views.hello,name='hello'),
    path('hm/<int:id>/',views.hm,name='hm'),
    path('task/<str:name>/<int:id>/',views.task,name='task'),
    path('basic/',views.basic,name='basic'),
    path('table/',views.table,name='table'),
    path('inline/',views.inline,name='inline'),
    path('internal/',views.internal,name='internal'),
    path('external/',views.external,name='external'),
    path('boot/',views.boot,name='boot'),
    path('offline/',views.offline,name='offline'),




    path('register/',views.register,name='register'),
    path('details/',views.details,name='details'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),


    path('reg/',views.reg,name='reg'),
    path('display/',views.display,name='display'),
    path('up/<int:id>/',views.up,name='up'),
    path('de/<int:id>/',views.de,name='de'),

    path('temp/',include('TempBlockApp.urls'))





]
