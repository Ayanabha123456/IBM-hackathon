from django.shortcuts import render,get_object_or_404
from .models import User, Cart, Item, Transaction
from django.template import loader
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def index(request):
    return render(request,'COVID/login.html')

def register(request):
    return render(request,'COVID/register.html')

def home(request):
    user=request.session.get('user')
    context={'user':user}
    return render(request,'COVID/index.html',context)

def registered(request):
    try:
        email=request.POST['email']
        password=request.POST['password']
        checkpass=request.POST['passwordcheck']
    except:
        return HttpResponseRedirect(reverse('COVID:register'))
    else:
        if password == checkpass:
            user = User(
                username=email,
                password=password
            )
            user.save()
            request.session['user']=email
            return HttpResponseRedirect(reverse('COVID:home'))
        else:
            return HttpResponseRedirect(reverse('COVID:register'))

def logged(request):
    try:
        username=request.POST['username']
        password=str(request.POST['password'])
    except:
        return HttpResponseRedirect(reverse('COVID:index'))
    else:
        try:
            user=User.objects.get(username=username)
            password1=user.password
        except:
            return HttpResponseRedirect(reverse('COVID:register'))
        else:
            request.session['user']=username
            return HttpResponseRedirect(reverse('COVID:home'))

def listed(request,cat):
    user=request.session.get('user')
    items=Item.objects.filter(category=cat)
    context={'user':user,'cate':cat,'items':items}
    return render(request,'COVID/list.html',context)

def add(request):
    try:
        itemname=request.POST.get('item')
        itemprice=int(request.POST['price'])
        itemquant=int(request.POST['quant'])
        cat=request.POST['cate']
    except:
        cat=request.POST['cate']
        return HttpResponseRedirect(reverse('COVID:home'))
    else:
        cart=Cart(name=itemname,price=itemprice,quantity=itemquant,category=cat)
        cart.save()
        return HttpResponseRedirect(reverse('COVID:listed',args=(cat,)))

def cart(request):
    try:
        things=Cart.objects.all()
    except:
        return HttpResponseRedirect(reverse('COVID:home'))
    else:
        total=0
        for thing in things:
            item1=Item.objects.get(name=thing.name)
            item1.stock=item1.stock-thing.quantity
            item1.save()
            total +=thing.quantity*thing.price
        context={'things':things,'total':total}
        return render(request,'COVID/cart.html',context)

def done(request):
    transact=Cart.objects.all()
    str=""
    for selection in transact:
        str=str+selection.name+"."
    fstr=str[:len(str)-1]
    transaction=Transaction(transact=fstr)
    transaction.save()
    transact_all=Transaction.objects.all()
    A=[]
    for i_transact in transact_all:
        L=i_transact.split(".")
        A.append(L)
    from apyori import apriori
    rules = apriori(L, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
    context={'rules':rules}
    transact.delete()
    return render(request,'COVID/suggestion.html',context)





