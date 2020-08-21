"""shopping_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from shoplist import views
import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #authentication
    path('signup/', views.usersignup, name='usersignup'),
    path('logout/', views.userlogout, name='userlogout'),
    path('login/', views.userlogin, name='userlogin'),
    path('create/', views.createlist, name='createlist'),
    path('shoplist/', views.currentshoplist, name='currentshoplist'),
    path('shoplist/<int:item_id>/', views.detail, name='detail'),
    path('shoplist/<int:item_id>/delete', views.deleteshop, name='deleteshop'),
    path('shoplist/<int:item_id>/createitem/', views.createitem, name='createitem'),
    path('shoplist/<int:item_id>/<int:things_id>', views.viewitems, name='viewitems'),
    path('shoplist/<int:item_id>/<int:things_id>/delete', views.deleteitem, name='deleteitem'),
    path('shoplist/<int:item_id>/<int:things_id>/complete', views.completeitem, name='completeitem'),
    path('shoplist/<int:item_id>/<int:things_id>/incomplete', views.incompleteitem, name='incompleteitem'),




]
