from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from datetime import date
from nturl2path import pathname2url
from random import randint
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.shortcuts import render
from django.db.models import Q, Sum
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def were(request):
    f= loader.get_template("werey.html")
    return HttpResponse(f.render({},request))
@login_required
def addc(request):
    f= loader.get_template("AddCustomer.html")
    if request.user== None:
        return redirect('login')
    if request.method == "POST" :
        d=randint(0000,9999)
        n=request.POST['first']+" "+request.POST['last']
        e=request.POST['mail']
        ph1=request.POST['ph1']
        ph2=request.POST['ph2']
        ad=request.POST['adds']
        reg=date.today()
        data=Customers(id=d,name=n,phone_no_1=ph1,phone_no_2=ph2,reg_date=reg,address=ad,mail=e)
        data.save()
        val=1
        u=Customers.objects.get(id=d)
        g=C_stat(customer=u)
        g.save()
        con={
            'value':val,
            'u':u
        }
        return HttpResponse(f.render(con,request))
    else:
        val=0
        con={
            'value':val
        }
        return HttpResponse(f.render(con,request))

    

@login_required
def c_list(request):
    f=loader.get_template("c_list.html")
    c_li=Customers.objects.all()
    if request.method == 'POST':
        query = request.POST['search']
        try:
            qq=int(query)
            results = Customers.objects.filter(
                Q(id__icontains=qq) | Q(name__icontains=query) | Q(mail__icontains=query) # Add more fields as needed
            )
        except ValueError:
            results = Customers.objects.filter(
                Q(name__icontains=query) | Q(mail__icontains=query) # Add more fields as needed
            )
        context = {'results': results}
        return HttpResponse(f.render(context,request))
    
    c_ids=[]
    for x in c_li:
        if len(c_ids)==0:
            c_ids.append(x)
        else:
            g=0
            for y in c_ids:
                if x.id < y.id:
                    c_ids.insert(g,x)
                    break
                g+=1
    con={
        'id':c_ids
    }

    return HttpResponse(f.render(con,request))

@login_required
def c_info(request,pk):
    f=loader.get_template("c_info.html")
    info=Customers.objects.get(id=pk)
    con={
        "info":info
    }
    return HttpResponse(f.render(con,request))

@login_required
def cstock(request,pk):
    if request.user== None:
        return redirect('login')
    f= loader.get_template("C_stockcard.html")
    cos=Customers.objects.get(id=pk)
    stat=C_stat.objects.get(customer=cos)
    it=items.objects.all()
    stock=Stock_card.objects.filter(c_id=cos)
    months=[]
    m_no=[]
    for x in stock:
        if x.date.strftime("%B") not in months:
            mm=x.date.month
            if len(m_no)==0:
                m_no.append(mm)
                months.append(x.date.strftime("%B"))
            else:
                t=0
                for y in m_no:
                    if mm < y:
                        months.insert(t, x.date.strftime("%B"))
                        m_no.insert(t, mm)
                        break
                    t+=1
    r_months={}
    i=0
    for m in m_no:
        filtered_months=stock.filter(date__month=m)
        a = filtered_months.aggregate(total=Sum('advance'))['total']
        o = filtered_months.aggregate(total=Sum('outstanding'))['total']
        p = filtered_months.aggregate(total=Sum('total_p'))['total']
        ml=[a,o,p]
        r_months.update({months[i]:ml})
        i+=1
    con={
        'cos':cos,
        'stock':stock,
        'it':it,
        'stat':stat,
        'months':months,
        'r_months':r_months
    }
    return HttpResponse(f.render(con,request))

@login_required
def cstock_reg(request,pk):
    if request.user== None:
        return redirect('login')
    cos_reg=Customers.objects.get(id=pk)
    stat=C_stat.objects.get(customer=cos_reg)
    d=date.today()
    dd=request.POST['fdata1']
    i=request.POST['fdata2']
    ii=items.objects.get(name=i)
    o=request.POST['fdata3']
    am= int(o)*ii.price
    ii.inventory=ii.inventory-int(o)
    ii.save()
    ad=request.POST['fdata5']
    bal= am-int(ad)
    out=request.POST['fdata7']
    total=am-int(out)
    mn=request.POST['fdata9']
    oi=randint(000,999)
    card=Stock_card(c_id=cos_reg,order_id=oi,date=dd,item=ii,order=o,amount=am,advance=ad,balance=bal,outstanding=out,total_p=total,means_of_Pay=mn)
    stat.advance=stat.advance+int(ad)
    stat.out=stat.out+int(out)
    stat.paid=stat.paid+total
    stat.save()
    card.save()
    return redirect('cstock', pk=pk)

@login_required
def home(request):
    f= loader.get_template("Home_page.html")
    
    if request.method == 'POST':
        query = request.POST['search']
        try:
            qq=int(query)
            results = Customers.objects.filter(
                Q(id__icontains=qq) | Q(name__icontains=query) | Q(mail__icontains=query) # Add more fields as needed
            )
        except ValueError:
            results = Customers.objects.filter(
                Q(name__icontains=query) | Q(mail__icontains=query) # Add more fields as needed
            )
        context = {'results': results}
        return HttpResponse(f.render(context,request))

    return HttpResponse(f.render({},request))