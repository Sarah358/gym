from django.shortcuts import render,redirect
import json 
from django.contrib.auth.decorators import login_required 
from .models import Location, Package, Booking
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse



 # Create your views here.

def search_gyms(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        location = Location.objects.filter(
            name__istartswith=search_str, owner=request.user) | Location.objects.filter(
            address__istartswith=search_str, owner=request.user)
        data = location.values()
        return JsonResponse(list(data), safe=False)


# show map
@login_required(login_url='/authentication/login')
def index(request): 
    location_list = list(Location.objects.order_by('name').values()) 
    location_json = json.dumps(location_list)  
    context = {'locations': location_json} 
    return render(request, 'gym/index.html', context) 

# gym details
@login_required(login_url='/authentication/login')
def gymdetails(request):
    location=Location.objects.all()
    paginator = Paginator(location, 8)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    

    context = {
        'location': location,
        'page_obj': page_obj,
        
    }
    return render(request,'gym/gymdetails.html', context)


# show packages
@login_required(login_url='/authentication/login')
def packages(request):
    # location=Location.objects.all()
    packages=Package.objects.all()
    paginator = Paginator(packages, 8)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    

    context = {
        'packages': packages,
        'page_obj': page_obj,
        
    }
    return render(request,'gym/packages.html', context)

# show bookings
@login_required(login_url='/authentication/login')
def bookings(request):
    # location=Location.objects.all()
    # bookings=Booking.objects.all()
    bookings = Booking.objects.filter(username=request.user)
    paginator = Paginator(bookings, 8)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    

    context = {
        'bookings': bookings,
        'page_obj': page_obj,
        
    }
    return render(request,'gym/bookings.html', context)

# book gym
@login_required(login_url='/authentication/login')
def book(request):
    packages=Package.objects.all()
    gymnames=Location.objects.all()
    context = {
        'packages': packages,
        'gymnames': gymnames,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'gym/book.html', context)

    if request.method == 'POST':
        name = request.POST['name']
        package = request.POST['package']
        gymname = request.POST['gymname']
        amount = request.POST['amount']
        phonenumber = request.POST['phonenumber']
        date = request.POST['book_date']

        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'gym/book.html', context)

        if not package:
            messages.error(request, 'Package is required')
            return render(request, 'gym/book.html', context)
        if not gymname:
            messages.error(request, 'GymName is required')
            return render(request, 'gym/book.html', context)
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'gym/book.html', context)
        if not phonenumber:
            messages.error(request, 'Phonenumber is required')
            return render(request, 'gym/book.html', context)

        Booking.objects.create(username=request.user, amount=amount, date=date,name=name,package=package,
                               gymname=gymname, phonenumber=phonenumber)
        messages.success(request, ' Gym Booked successfully')
        return redirect('bookings')

#  edit bookings
def edit_book(request, id):
    booking = Booking.objects.get(pk=id)
    packages=Package.objects.all()
    gymnames=Location.objects.all()
    context = {
        'booking': booking,
        'values': booking,
        'packages': packages,
        'gymnames': gymnames,
    }
    if request.method == 'GET':
        return render(request, 'gym/edit-book.html', context)
    if request.method == 'POST':

        name = request.POST['name']
        package = request.POST['package']
        gymname = request.POST['gymname']
        amount = request.POST['amount']
        phonenumber = request.POST['phonenumber']
        date = request.POST['book_date']

        if not name:
            messages.error(request, 'Name is required')
            return render(request, 'gym/book.html', context)
        if not package:
            messages.error(request, 'Package is required')
            return render(request, 'gym/book.html', context)
        if not gymname:
            messages.error(request, 'GymName is required')
            return render(request, 'gym/book.html', context)
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'gym/book.html', context)
        if not phonenumber:
            messages.error(request, 'Phonenumber is required')
            return render(request, 'gym/book.html', context)

        booking.username = request.user
        booking.name = name
        booking.package = package
        booking.gymname = gymname
        booking.amount = amount
        booking. phonenumber = phonenumber
        booking. date = date
        

        booking.save()
        messages.success(request, 'Booking updated  successfully')

        return redirect('bookings')

def delete_book(request, id):
    booking = Booking.objects.get(pk=id)
    booking.delete()
    messages.success(request, 'Booking  removed')
    return redirect('bookings')