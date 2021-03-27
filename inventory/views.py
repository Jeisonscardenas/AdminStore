from django.shortcuts import render, redirect
from .models import *
from .forms import *



def index(request):

    return render (request, 'index.html')

#Manage Distributors

def showDistributor(request):

    distributors = Distributor.objects.all()
    ctx = { 'distributors': distributors,}

    return render (request, 'distributor.html', ctx)

def createDistributor(request):
    if request.method == 'GET':
        form = FormDistributor()
        ctx = {
            'form': form
        }
    else:
        form = FormDistributor(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Distributor')

    return render(request, 'manage_distributor.html', ctx)

def editDistributor (request, id):

    distributor = Distributor.objects.get(id = id)

    if request.method == 'GET':
        form = FormDistributor (instance = distributor)
        ctx = {
            'form': form
        }
    else:
        form = FormDistributor (request.POST, instance=distributor)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Distributor')

    return render(request, 'manage_distributor.html', ctx)


def deleteDistributor(request, id):

    distributor = Distributor.objects.get(id = id)
    distributor.delete()
    return redirect('show_Distributor')


#Manage Item

def showItem(request):

    items = Item.objects.all()
    ctx = { 'items': items,}

    return render (request, 'item.html', ctx)

def createItem(request):
    if request.method == 'GET':
        form = FormItem()
        ctx = {
            'form': form
        }
    else:
        form = FormItem(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Item')

    return render(request, 'manage_item.html', ctx)

def editItem (request, id):

    item = Item.objects.get(id = id)

    if request.method == 'GET':
        form = FormItem (instance = item)
        ctx = {
            'form': form
        }
    else:
        form = FormItem (request.POST, instance=item)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Item')

    return render(request, 'manage_item.html', ctx)


def deleteItem(request, id):

    item = Item.objects.get(id = id)
    item.delete()
    return redirect('show_Item')


#Manage User

def showUser(request):

    users = User.objects.all()
    ctx = { 'users': users,}

    return render (request, 'user.html', ctx)

def createUser(request):
    if request.method == 'GET':
        form = FormUser()
        ctx = {
            'form': form
        }
    else:
        form = FormUser(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_User')

    return render(request, 'manage_user.html', ctx)

def editUser (request, id):

    user = User.objects.get(id = id)

    if request.method == 'GET':
        form = FormUser (instance = user)
        ctx = {
            'form': form
        }
    else:
        form = FormUser (request.POST, instance=user)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_User')

    return render(request, 'manage_user.html', ctx)


def deleteUser(request, id):

    user = User.objects.get(id = id)
    user.delete()
    return redirect('show_User')

#Manage Invoice

def showInvoice(request):

    invoices = Invoice.objects.all()
    ctx = { 'invoices': invoices,}

    return render (request, 'invoice.html', ctx)

def createInvoice(request):
    if request.method == 'GET':
        form = FormInvoice()
        ctx = {
            'form': form
        }
    else:
        form = FormInvoice(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Invoice')

    return render(request, 'manage_invoice.html', ctx)

def editInvoice (request, id):

    invoice = Invoice.objects.get(id = id)

    if request.method == 'GET':
        form = FormInvoice (instance = invoice)
        ctx = {
            'form': form
        }
    else:
        form = FormInvoice (request.POST, instance=invoice)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Invoice')

    return render(request, 'manage_invoice.html', ctx)


def deleteInvoice(request, id):

    invoice = Invoice.objects.get(id = id)
    invoice.delete()
    return redirect('show_Invoice')

#Manage Point

def showPoint(request):

    points = Point.objects.all()
    ctx = { 'points': points,}

    return render (request, 'point.html', ctx)

def createPoint(request):
    if request.method == 'GET':
        form = FormPoint()
        ctx = {
            'form': form
        }
    else:
        form = FormPoint(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Point')

    return render(request, 'manage_point.html', ctx)

def editPoint (request, id):

    point = Point.objects.get(id = id)

    if request.method == 'GET':
        form = FormPoint (instance = point)
        ctx = {
            'form': form
        }
    else:
        form = FormPoint (request.POST, instance=point)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Point')

    return render(request, 'manage_point.html', ctx)


def deletePoint(request, id):

    point = Point.objects.get(id = id)
    point.delete()
    return redirect('show_Point')

    #Manage Details Invoice

def showDetail(request):

    details_invoice = Detail_invoice.objects.all()
    ctx = { 'details_invoice': details_invoice,}

    return render (request, 'detail_invoice.html', ctx)

def createDetail(request):
    if request.method == 'GET':
        form = FormDetail()
        ctx = {
            'form': form
        }
    else:
        form = FormDetail(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Detail')

    return render(request, 'manage_detail.html', ctx)

def editDetail (request, id):

    detail = Detail_invoice.objects.get(id = id)

    if request.method == 'GET':
        form = FormDetail (instance = detail)
        ctx = {
            'form': form
        }
    else:
        form = FormDetail (request.POST, instance=detail)
        ctx = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('show_Detail')

    return render(request, 'manage_detail.html', ctx)


def deleteDetail(request, id):

    detail = Detail_invoice.objects.get(id = id)
    detail.delete()
    return redirect('show_Detail')



# Create your views here.
