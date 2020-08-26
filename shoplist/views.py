from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ShopForm, ItemForm
from .models import Shoplist, Items
from django.utils import timezone

# Create your views here.
def usersignup(request):
    if request.method == 'GET':
        return render(request, 'shoplist/usersignup.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentshoplist')

            except IntegrityError:
                    return render(request, 'shoplist/usersignup.html', {'form':UserCreationForm(), 'error':'The username has already been taken'})

        else:
            return render(request, 'shoplist/usersignup.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def userlogin(request):
    if request.method == 'GET':
        return render(request, 'shoplist/userlogin.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'shoplist/userlogin.html', {'form':AuthenticationForm(), 'error':'Username or Password did not match'})
        else:
            login(request, user)
            return redirect('currentshoplist')

def createlist(request):
    if request.method == 'GET':
        return render(request, 'shoplist/createlist.html', {'form':ShopForm()})
    else:
        try:
            form = ShopForm(request.POST)
            shoplist = form.save(commit=False)
            shoplist.user = request.user
            shoplist.save()
            return redirect('currentshoplist')
        except ValueError:
            return render(request, 'shoplist/createlist.html', {'form':ShopForm()})


def home(request):
    return render(request, 'shoplist/home.html')


def createitem(request, item_id):
    if request.method == 'GET':
        return render(request, 'shoplist/createitem.html', {'form':ItemForm(), 'id':item_id})
    else:
        try:
            form = ItemForm(request.POST)
            itemlist = form.save(commit=False)
            itemlist.shoplist = Shoplist.objects.filter(user=request.user, pk=item_id).first()
            itemlist.user = request.user
            itemlist.save()
            return redirect('detail', item_id=item_id)
        except ValueError:
            return render(request, 'shoplist/createitem.html', {'form':ItemForm()})

def currentshoplist(request):
    shoplist = Shoplist.objects.filter(user=request.user).order_by('-created')
    return render(request, 'shoplist/currentshoplist.html', {'shoplist':shoplist})

def detail(request, item_id):
    shopitems = get_object_or_404(Shoplist, pk=item_id)
    item = Items.objects.filter(user=request.user, shoplist=item_id)
    return render(request, 'shoplist/detail.html', {'shopitems': shopitems, 'item':item, 'item_id': item_id})

def viewitems(request, item_id, things_id):
    shopitem = get_object_or_404(Items, pk=things_id, user=request.user)
    item = Items.objects.filter(user=request.user, shoplist=item_id)
    if request.method == 'GET':         
        form = ItemForm(instance=shopitem)
        return render(request,'shoplist/viewitems.html', {'shopitem':shopitem, 'form':form, 'item':item, 'item_id':item_id})
    else:
        try:
            form = ItemForm(request.POST, instance=shopitem)
            form.save()            
            return redirect('detail', item_id=item_id)
        except ValueError:
            return render(request,'shoplist/viewitems.html', {'shopitem':shopitem, 'form':form, 'item_id':item_id})

def completeitem(request, item_id, things_id):
    shopitem = get_object_or_404(Items, pk=things_id, user=request.user)
    if request.method == 'POST':
        shopitem.datecompleted = timezone.now()
        shopitem.save()
        return redirect('detail', item_id=item_id)

def incompleteitem(request, item_id, things_id):
    shopitem = get_object_or_404(Items, pk=things_id, user=request.user)
    if request.method == 'POST':
        shopitem.datecompleted = None
        shopitem.save()
        return redirect('detail', item_id=item_id)

def deleteitem(request, item_id, things_id):
    shopitem = get_object_or_404(Items, pk=things_id, user=request.user)
    if request.method == 'POST':
        shopitem.delete()
        return redirect('detail', item_id=item_id)

def deleteshop(request, item_id):
    shopitems = get_object_or_404(Shoplist, pk=item_id)
    shopitems.delete()
    return redirect('currentshoplist')